from django.urls import reverse
from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    prod_description = models.TextField(max_length=255)
    price = models.IntegerField()
    prod_image = models.ImageField(upload_to='photos/products/')
    stock = models.IntegerField()
    prod_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField()

    
    def get_url(self):
        return reverse("product_detail", args = [self.prod_category.slug, self.slug])
    
    def __str__(self):
        return self.product_name
        