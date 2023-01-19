from django.db import models
from menu.models import FoodItem
from accounts.models import User


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantities = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.user

class Tax(models.Model):
    tax_type = models.CharField(max_length=20,unique=True)
    tax_percentage = models.DecimalField(decimal_places=2,max_digits=4,verbose_name='tax percentage(%)')
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.tax_type

