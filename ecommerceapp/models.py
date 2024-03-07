from django.db import models
from django.contrib.auth.models import User            

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=255)
  
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    productname=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=255,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    pimage=models.ImageField(default="default1.jpg",blank=True,upload_to="image/", null=True)
    
class Usermember(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,null=True)
    number=models.CharField(max_length=255,null=True)
    image=models.ImageField(default="default1.jpg",blank=True,upload_to="image/", null=True)

class Cart(models.Model): 
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   
