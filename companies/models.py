# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from materials.models import Materials

# Create your models here.



class Price(models.Model):
    price = models.IntegerField(default=0)
    volume = models.IntegerField(default=0, verbose_name='Maximum volume')

    def __str__(self):
        return 'Price: %d for a maximum volume of %d' % (self.price, self.volume)

class Companies(models.Model):
    name = models.CharField(max_length=50)
    materials = models.ManyToManyField(Materials, related_name='companies')
    prices = models.ManyToManyField(Price, related_name='companies')

    def __str__(self):
        return self.name
        