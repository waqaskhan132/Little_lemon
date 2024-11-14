from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serilizer import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
 # Create your views here.
 
 # booking view 
class bookingview(APIView):
    # one way to do that
    def get(self, request):
        item= Booking_table.objects.all()
        serilize=booking_tableSerilizer(item, many=True)
        return Response(serilize.data)
        
    def post(self , request):
        serlize= booking_tableSerilizer(data=request.data)
        if serlize.is_valid():
            serlize.save()
            return Response({"status":"succes","data":serlize.data})     

#othereway to do this will give gui on addmin panel 
class menuview(generics.ListCreateAPIView):
    
    queryset = Menu_table.objects.all()
    serializer_class = menu_tableSerilizer
    '''def get(self,request):
        menu=Menu_table.objects.all()
        serlize= menu_tableSerilizer(menu, many=True)
        return Response(serlize.data)
    
    def post(self , request):
        serlize= menu_tableSerilizer(data=request.data)
        if serlize.is_valid():
            serlize.save()
            return Response({"status":"succes","data":serlize.data})'''
        
class menusingleview(generics.UpdateAPIView,generics.DestroyAPIView,generics.ListAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = menu_tableSerilizer
    
# another way to do this using viewset 

class bookingviewset(viewsets.ModelViewSet):
    queryset = Menu_table.objects.all()
    serializer_class = menu_tableSerilizer
    permission_classes = [permissions.IsAuthenticated]


@api_view()
@permission_classes([permissions.IsAuthenticated])
def msgview(request):
    return Response({"msg":"This is authenticated class permission"})
    
    