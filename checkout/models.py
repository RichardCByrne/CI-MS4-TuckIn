import uuid
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.db.models.deletion import CASCADE, RESTRICT
from restaurants.models import Restaurant, FoodItem
from profiles.models import CustomerProfile

class Order(models.Model):
    # Referenced Boutique Ado
    order_number = models.CharField(max_length=32, null=False, editable=False)
    order_restaurant = models.ForeignKey(Restaurant, max_length=64, null=False, on_delete=RESTRICT)
    customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_1 = models.CharField(max_length=80, null=False, blank=False)
    address_2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')

    # From Boutique Ado
    def _generate_order_number():
        return uuid.uuid4().hex.upper()

    # Referenced Boutique Ado
    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.delivery_cost = self.order_restaurant.delivery_cost
        self.grand_total = self.delivery_cost + self.order_total
        self.save()

    # From Boutique Ado
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    # From Boutique Ado
    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    # Referenced Boutique Ado
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=CASCADE, related_name='lineitems')
    food_item = models.ForeignKey(FoodItem, null=False, blank=False, on_delete=RESTRICT)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    # From Boutique Ado
    def save(self, *args, **kwargs):
        self.lineitem_total = self.food_item.price * self.quantity
        super().save(*args, **kwargs)

    # Referenced Boutique Ado
    def __str__(self):
        return f'SKU {self.food_item.friendly_name} on order {self.order.order_number}'