from django.db import models

# Create your models here.

class Booking_table(models.Model ):
    Name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField(max_length=6)
    BookingDate=models.DateField()


class Menu_table(models.Model):
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=5, decimal_places=2)
    Inventory=models.IntegerField(max_length=5)
    
