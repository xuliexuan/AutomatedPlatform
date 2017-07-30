from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32) #max length is 32, and type is char
    pwd = models.CharField(max_length=32)
