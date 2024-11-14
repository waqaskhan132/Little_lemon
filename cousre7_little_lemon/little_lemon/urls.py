
from django.contrib import admin
from django.urls import path,include
from .views import *
from .views import bookingviewset
from  rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('booking', bookingview.as_view(),name="booking"),
    path('menu',menuview.as_view(),name="menu"),
    path('menu-single/<int:pk>',menusingleview.as_view(),name="menusingle"),
    path('msg',msgview,name="view"),
    path('token',obtain_auth_token,name="view"),
]