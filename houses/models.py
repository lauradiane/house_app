from django.db import models

class Owner(models.Model):
    name = models.TextField()

class House(models.Model):
    address = models.TextField()
    owner = models.OneToOneField(Owner) #one to one field with Owner.

