from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_title
    
class Product(models.Model):
    product_title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='media/products/images/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField()
    discription = models.TextField(max_length=400)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_title