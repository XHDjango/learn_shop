# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2019-09-17 19:33:31
@Description: 
"""

from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("home/", views.home, name="home"),
]
