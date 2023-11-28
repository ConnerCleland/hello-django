# urls.py
from django.urls import path
from app.views import hello_view, hey_view, age_in_view, order_total_view

urlpatterns = [
    path("hello/", hello_view, name="hello_view"),
    path("hey/", hey_view, name="hey_view"),
    path("age/", age_in_view, name="age_in_view"),
    path("order/", order_total_view, name="order_total_view"),
]
