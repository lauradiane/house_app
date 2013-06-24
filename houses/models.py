from django.db import models

class OwnerManager(models.Manager):
    def create_owner(self, new_name):
        new_owner = self.create(name=new_name)
        new_owner.save()
        print 'Added owner: name=[%s]' % new_name
        return new_owner

class Owner(models.Model):
    name = models.TextField()
    objects = OwnerManager()

class House(models.Model):
    address = models.TextField()
    owner = models.OneToOneField(Owner) #one to one field with Owner.

