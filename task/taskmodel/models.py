from django.db import models

# Create your models here.

class User(models.Model):
    userid=models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    age = models.DateField(auto_now_add=True,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
class Schedule(models.Model):
    scheduleid = models.AutoField(primary_key=True)
    # userid = models.IntegerField()
    scheduledate = models.DateField(auto_now_add=True)
    scheduletime = models.TimeField(auto_now_add=True)
    scheduleevent = models.CharField(max_length=1000)
    done = models.BooleanField(auto_created=False)
    username = models.CharField(max_length=20)
class Note(models.Model):
    noteid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    note = models.CharField(max_length=1000,blank=True,null=True)