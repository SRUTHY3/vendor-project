from django.db import models

# Create your models here.
class user_tb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    place=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name