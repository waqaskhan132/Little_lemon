
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('booking', bookingview.as_view(),name="booking"),
    path('menu',menuview.as_view(),name="menu"),
    path('menu-single/<int:pk>',menusingleview.as_view(),name="menusingle"),
]