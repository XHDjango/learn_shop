from django.shortcuts import render

from .models import Car


# Create your views here.
def home(request):
    main_shop = Car.objects.all().filter(type="shop")
    data = {
        "title": "首页",
        "main_wheels": Car.objects.all().filter(type="wheel"),
        "main_navs": Car.objects.all().filter(type="nav"),
        "main_mustbys": Car.objects.all().filter(type="mustby"),
        "main_shop0": main_shop[0],
        "main_shop1_2": main_shop[1:3],
        "main_shop3_6": main_shop[3:7],
        "main_shop7_10": main_shop[7:11],
    }
    return render(request, "main/home.html", context=data)


def market(request):
    return render(request, "main/market.html")


def cart(request):
    return render(request, "main/cart.html")


def mine(request):
    return render(request, "main/mine.html")
