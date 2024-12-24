from django.db import models

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    listed_date = models.DateField(auto_now_add=True)

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

class Listing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Sold', 'Sold')],
        default='Pending'
    )
    created_date = models.DateField(auto_now_add=True)
