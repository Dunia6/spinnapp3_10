from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Marketplace(models.Model):
    """ La classe de la marketplace """
    name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='marketplace/avatar/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_time']
    
    