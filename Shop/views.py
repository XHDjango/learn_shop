from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop, Car


# Create your views here.
def home(request):
    all = Shop.objects.all()
    data = {
        "title": "首页",
        "main_wheels": Car.objects.all(),
        "main_navs":all[5:9],
    }
    return render(request, "main/home.html", context=data)


def market(request):
    return render(request, "main/market.html")


def cart(request):
    return render(request, "main/cart.html")


def mine(request):
    return render(request, "main/mine.html")
