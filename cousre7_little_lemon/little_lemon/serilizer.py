from rest_framework import serializers

from .models import *

class booking_tableSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking_table
        fields="__all__"



class menu_tableSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu_table
        fields="__all__"
