from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.http import StreamingHttpResponse
from django.urls import reverse
from django.core import serializers
from collections import Counter
from .models import *
import json
import time
from .globals import new_data_queue

# Create your views here.

def index(request):
    if request.user and request.user.is_authenticated:
        return HttpResponseRedirect(reverse("menu_select"))
    return render(request, "pos_server/index.html", {
        "route":"login"
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("pos"))
        else:
            return render(request, "pos_server/index.html", {
                "route":"login",
                "failed_login":True
            })

def kitchen(request):
    if request.method == "GET":
        # Fetch all orders
        orders = Order.objects.all()

        # Prepare data for each order
        orders_data = []
        for order in orders:
            orders_data.append(collect_order(order))
        # print(orders_data)
        return render(request, "pos_server/queue.html", {
            "route":"kitchen",
            'orders': orders_data,
            "portrait" : request.GET.get('portrait', 'false') == 'true'
        })
    elif request.method == "DELETE":
        order_id = json.loads(request.body)["orderId"]
        order = Order.objects.get(id=order_id)
        order.delete()
        return JsonResponse({"status":"Order deleted"}, status=200)
    
def menu_select(request):
    menus = Menu.objects.all()
    return render(request, "pos_server/menu_select.html", {
            "route":"menu_select",
            "menus":menus
        })

def pos(request, menu):
    if request.method == "GET":
        print(menu)
        dishes = Dish.objects.filter(menu=Menu.objects.filter(title = menu).first())
        print(dishes)
        return render(request, "pos_server/order.html", {
            "route":"pos",
            "menu": dishes,
            "menu_title": menu,
            "json": serializers.serialize('json', dishes)
        })
    elif request.method == "POST":
        body = json.loads(request.body)
        order = body["order"]
        dish_counts = Counter(order)
        new_order = Order()
        new_order.table = body["table"] if body["table"].strip() != '' else None
        new_order.save()
        for dish_id, quantity in dish_counts.items():
            dish = Dish.objects.get(id=dish_id)
            order_dish = OrderDish(order=new_order, dish=dish, quantity=quantity)
            order_dish.save()
        return JsonResponse({"Message":"Sent to kitchen"}, status=200)

def event_stream():
    while True:
        while new_data_queue:
            data = new_data_queue.pop(0)
            order_data_json = json.dumps(collect_order(data))
            print("sending dish")
            yield f"data: {order_data_json}\n\n"
        # Send a heartbeat every X seconds
        yield "\n"
        time.sleep(1)


def order_updates(request):
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    # response['Cache-Control'] = 'no-cache'
    return response

def collect_order(order):
    # Fetch related OrderDish instances for each order
    order_dishes = OrderDish.objects.filter(order=order)

    # Prepare dish details for this order
    dishes_data = [{
        'name': od.dish.title,
        'quantity': od.quantity
    } for od in order_dishes]

    # Add the order and its dishes to the orders_data list
    return({
        'order_id': order.id,
        'dishes': dishes_data,
        'table':order.table
    })