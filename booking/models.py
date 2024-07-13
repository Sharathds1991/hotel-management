from django.db import models

from users.models import CustomUser

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, 
    )
    description= models.TextField(blank=True, null=True)
    price_per_day=models.IntegerField()
    available = models.BooleanField(default = False)
    
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, 
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Client_booking(models.Model):
    name = models.CharField(max_length=255)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, 
    )
    cost=models.IntegerField()
    days=models.IntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, 
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)