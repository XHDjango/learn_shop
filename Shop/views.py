from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop


# Create your views here.
def home(request):
    all = Shop.objects.all()
    data = {
        "title": "首页",
        "main_wheels": all[:5],
    }
    return render(request, "main/home.html", context=data)


def market(request):
    return render(request, "main/market.html")


def cart(request):
    return render(request, "main/cart.html")


def mine(request):
    return render(request, "main/mine.html")
