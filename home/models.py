from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class signupit(models.Model):
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=32)

def __str__(self):
    return self.email

class mobile_spec(models.Model):
    mobile_pic=models.ImageField(upload_to='mobiles/pics')
    model=models.CharField(max_length=100)
    price=models.IntegerField()
    discription=models.CharField(max_length=250)
    #def __str__(self):
        # return self.model

class cart(models.Model):
    cart_models=models.ManyToManyField(mobile_spec)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class buy_mobiles(models.Model):
    cart_models=models.ManyToManyField(mobile_spec)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True)
    address=models.TextField(max_length=250,null=True)



    
