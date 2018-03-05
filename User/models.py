from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10)
    wechat = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.CharField(max_length=30)
    company = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200)
    count = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=10000)
    website = models.CharField(max_length=255)
    following = models.BigIntegerField(max_length=None)
    follower = models.BigIntegerField(max_length=None)


    class Meta:
        managed = False
        db_table = 'user'

class Follow(models.Model):
    id = models.IntegerField(primary_key=True)
    fromuser = models.CharField(max_length=255)
    touser = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'follow' 
