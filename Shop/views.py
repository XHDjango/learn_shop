from django.shortcuts import render

from .models import Car


# Create your views here.
def home(request):
    data = {
        "title": "首页",
        "main_wheels": Car.objects.all().filter(type="wheel"),
        "main_navs": Car.objects.all().filter(type="nav"),
        "main_mustbys": Car.objects.all().filter(type="mustby"),
    }
    return render(request, "main/home.html", context=data)


def market(request):
    return render(request, "main/market.html")


def cart(request):
    return render(request, "main/cart.html")


def mine(request):
    return render(request, "main/mine.html")
