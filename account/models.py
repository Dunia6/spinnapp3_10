from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """ La classe du profile """
    first_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username