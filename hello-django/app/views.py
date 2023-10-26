from django.http.response import HttpResponse
from django.http.request import HttpRequest
from datetime import datetime


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


def hey_view(request, name):
    upper = name.upper()
    user_name = f"Hey, {upper}!"
    return HttpResponse(user_name)


def age_in_view(request: HttpRequest, end: int, birthday: int) -> HttpResponse:
    age = end - birthday
    text = f"{age}"
    return HttpResponse(text)


def order_total_view(request, burgers, fries, drinks):
    burgers = int(burgers)
    fries = int(fries)
    drinks = int(drinks)

    burgers_price = 4.50
    fries_price = 1.50
    drinks_price = 1.00

    total = (burgers * burgers_price) + (fries * fries_price) + (drinks * drinks_price)

    return HttpResponse(f"Total: ${total:.2f}")
