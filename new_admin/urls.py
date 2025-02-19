from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="admin-index"),


    path("dashboard", views.dashboard, name="admin-dashboard"),
    path("dashboard/home", views.dashboard_home, name="admin-dashboard-home"),

    path("orders", views.orders, name="admin-orders"),
    path("orders/retail", views.retail_orders, name="admin-orders-retail"),
    path("orders/retail/<int:id>", views.retail_order, name="admin-order-retail"),
    path("orders/retail/<int:id>/receipt", views.receipt, name="admin-index"),
    
    path("store", views.store, name="admin-store"),
    path("store/promo-content", views.promo_content, name="admin-store-promo-content"),
    path("store/promo-content/<int:id>", views.promo_content_instance, name="admin-store-promo-content-instance"),
    path("store/promo-content/new", views.promo_content_new, name="admin-store-promo-content-new"),
    path("store/branding", views.store_branding, name="admin-store-branding"),
]