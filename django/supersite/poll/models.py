from django.db import models

# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=255, null=True)
    family = models.CharField(max_length=255, null=True)
    post_card = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
