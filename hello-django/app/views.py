# views.py
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime
from .forms import AgeForm, OrderForm


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


def hey_view(request: HttpRequest):
    user_name = None

    if request.method == "POST":
        raw_name = request.POST.get("name", None)
        user_name = raw_name.upper() if raw_name else None

    return render(request, "hey_view.html", {"user_name": user_name})


def age_in_view(request: HttpRequest):
    age = None

    if request.method == "POST":
        form = AgeForm(request.POST)
        if form.is_valid():
            end = form.cleaned_data["end"]
            birthday = form.cleaned_data["birthday"]

            age = end - birthday

    else:
        form = AgeForm()

    return render(request, "age_form.html", {"form": form, "age": age})


def order_total_view(request):
    total = None

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            burgers = form.cleaned_data["burgers"]
            fries = form.cleaned_data["fries"]
            drinks = form.cleaned_data["drinks"]

            burgers_price = 4.50
            fries_price = 1.50
            drinks_price = 1.00

            total = (
                (burgers * burgers_price)
                + (fries * fries_price)
                + (drinks * drinks_price)
            )

    else:
        form = OrderForm()

    return render(request, "order_form.html", {"form": form, "total": total})
