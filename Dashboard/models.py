from __future__ import unicode_literals
from User.models import *
from django.db import models


# Create your models here.

class Warehouse(models.Model):
    workid = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, models.CASCADE, db_column='username', blank=True, null=True,to_field="username")
    title = models.CharField(max_length=255)
    opendate = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    cox = models.DecimalField(max_length=65, max_digits=10, decimal_places=2)
    coy = models.DecimalField(max_length=65, max_digits=10, decimal_places=2)
    coz = models.DecimalField(max_length=65, max_digits=10, decimal_places=2)
    cax = models.DecimalField(max_length=65, max_digits=10, decimal_places=2)
    cay = models.DecimalField(max_length=65, max_digits=10, decimal_places=2)
    caz = models.DecimalField(max_length=65, max_digits=10, decimal_places=2)
    
    status = models.SmallIntegerField()
    type = models.CharField(max_length=200)
    view = models.BigIntegerField(max_length=None)
    like = models.BigIntegerField(max_length=None)
    share = models.BigIntegerField(max_length=None)


    class Meta:
        managed = False
        db_table = 'warehouse'

