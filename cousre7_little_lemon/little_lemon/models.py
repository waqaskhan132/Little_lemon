from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Booking_table(models.Model ):
    Name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    BookingDate=models.DateField()
    
    def __str__(self):
        return self.Name


class Menu_table(models.Model):
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=5, decimal_places=2)
    Inventory=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return self.Title
    
