
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from little_lemon.views import bookingviewset,index
route=routers.DefaultRouter()
route.register(r'tables', bookingviewset)
urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('little_lemon.urls')),
    path('api/', include(route.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
   
]
