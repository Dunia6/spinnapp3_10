from django.db import models

from marketplace.models import Marketplace
# Create your models here.

class Category(models.Model):
    """ La classe de la category """
    name = models.CharField(max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    """ La classe de l'article """
    main_image = models.ImageField(upload_to='articles/images/', blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-created_time']


class ArticleImage(models.Model):
    """ Model for storing additional article images """
    image = models.ImageField(upload_to='articles/images/', blank=True)
    article = models.ForeignKey(Article, related_name='additional_images', on_delete=models.CASCADE)