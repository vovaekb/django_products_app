from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    published = models.BolleanField()
    deleted = models.BolleanField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80)
    products = models.ManyToManyField(Product)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
