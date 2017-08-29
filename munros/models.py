# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mountain(models.Model):
  name= models.CharField(max_length= 200, null= False, blank= False, unique= True)
  height= models.CharField(max_length=20)
  lat= models.DecimalField(max_digits=9, decimal_places=6)
  lon= models.DecimalField(max_digits=9, decimal_places=6)
  created_at= models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s %s' % (self.name, self.height) 

class Images(models.Model):
  image= models.CharField(max_length= 255, null= True, blank= True),