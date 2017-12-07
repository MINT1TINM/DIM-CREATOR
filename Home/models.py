from __future__ import unicode_literals
from User.models import *
from Dashboard.models import *
from django.db import models

# Create your models here.

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    workid = models.ForeignKey(Warehouse, models.CASCADE, db_column='workid', blank=True, null=True,to_field="workid")
    username = models.ForeignKey(User, models.CASCADE, db_column='username', blank=True, null=True,to_field="username")
    content = models.CharField(max_length=10000)
    time = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'comment'
