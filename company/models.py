from django.db import models

# Create your models here.
class company_tb(models.Model):
    name = models.CharField(max_length=100)
    bname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    place=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    dist=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    state=models.CharField(max_length=100)
    bimg=models.ImageField(upload_to="bimg")
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Com_mssg(models.Model):
    mssg=models.CharField(max_length=600)
    Companyid=models.ForeignKey(company_tb,on_delete=models.CASCADE)
    approve=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    
    def __str__(self):
        return self.mssg 
    