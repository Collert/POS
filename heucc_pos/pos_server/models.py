from django.db import models

# Create your models here.
    
class Menu(models.Model):
    title = models.CharField(max_length=140)

    def __str__(self) -> str:
        return f"Menu: {self.title}"

class Dish(models.Model):
    title = models.CharField(max_length=140)
    price = models.FloatField()
    menu = models.ForeignKey("Menu", on_delete = models.CASCADE, related_name = "dishes")

    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    dishes = models.ManyToManyField(Dish, through="OrderDish")
    table = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"Order {self.id}"

class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} X {self.dish.title} in order {self.order.id}"