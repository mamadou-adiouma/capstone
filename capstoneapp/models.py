from django.db import models


# Create your models here.


# Test model
def __str__(self):
    return f"{self.title} : {self.price}"


# Serializeurs (auth - token)
class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f"{self.title} : {str(self.price)}"

    # Test model
    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=True)
