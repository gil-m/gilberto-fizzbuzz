# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import fizzbuzz


urlpatterns = [
    path('<int:number>', fizzbuzz, name='fizzbuzz'),
]
