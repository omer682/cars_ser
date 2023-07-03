from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    person_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    city = models.CharField(max_length=255,null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    

    
    # Override related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='person_set',
        related_query_name='person',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='person_set',
        related_query_name='person',
    )
    def __str__(self):
        return f"{self.username}"


class Car(models.Model):
    plate_id = models.CharField(unique=True, max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    km = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    gearbox = models.CharField(max_length=255)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"id : {self.plate_id} manufacturer : {self.manufacturer}"

class Rent(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Person, on_delete=models.CASCADE)


class ContactUs(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    message = models.TextField(max_length=700)