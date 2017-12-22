from __future__ import unicode_literals
from User.models import *
from Dashboard.models import *
from django.db import models

# Create your models here.

class Comment_Product(models.Model):
    id = models.IntegerField(primary_key=True)
    workid = models.ForeignKey(Warehouse, models.CASCADE, db_column='workid', blank=True, null=True,to_field="workid")
    username = models.ForeignKey(User, models.CASCADE, db_column='username', blank=True, null=True,to_field="username")
    content = models.CharField(max_length=10000)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'comment'

class View_Product(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    workid = models.ForeignKey(Warehouse, models.CASCADE, db_column='workid', blank=True, null=True,to_field="workid")
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'view'

class Like_Product(models.Model):
    id = models.IntegerField(primary_key=True)
    workid = models.ForeignKey(Warehouse, models.CASCADE, db_column='workid', blank=True, null=True,to_field="workid")
    username = models.ForeignKey(User, models.CASCADE, db_column='username', blank=True, null=True,to_field="username")
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'like'

class Share_Product(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    workid = models.ForeignKey(Warehouse, models.CASCADE, db_column='workid', blank=True, null=True,to_field="workid")
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'share'        

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    publishdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'news'