from django.test import TestCase
from little_lemon.models import *

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu_table.objects.create(Title="IceCream", Price=80.00, Inventory=10)
        
        self.assertEqual(item.__str__(), "IceCream : 80.0")