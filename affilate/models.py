from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('Education','Education'),
        ('Technology & Gadgets','Technology & Gadgets'),
        ('Smartphone & Tablets','Smartphone & Tablest'),
        ('Automobile','Automobile'),
        ('Other','Other')
    )
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='Products')
    price = models.FloatField()
    link = models.URLField()
    category = models.CharField(max_length=200, choices=CATEGORY,default='Other')