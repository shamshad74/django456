from enum import unique
from operator import mod
from django.db import models

# Create your models here.

class Mobiles(models.Model):
    name=models.CharField(max_length=100,unique=True)
    brand=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    specs=models.CharField(max_length=200)
    band=models.CharField(max_length=100)


    def __str__(self):
        return self.name




# all mobiles exclude samsung
# qs=Mobiles.objects.all().exclude(brand="samsung")

# qs=Mobiles.objects.filter(band__iexact="4g")

# qs=Mobiles.objects.filter(name__contains="a")

# update
# Mobiles.objects.filter(id=1).update(band="4G")

# delete
#  Mobiles.objects.filter(id=4).delete()


# create create()
# list all()
# filter filter()
# > __gt
# >= __gte
# < __lt
# <= __lte
# __iexact
# __icontains
# 
# 