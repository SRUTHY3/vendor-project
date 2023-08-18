from django.db import models

# Create your models here.
class projectadmin(models.Model):
    name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)
    def __str__(self) :
        return self.name