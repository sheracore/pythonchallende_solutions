from django.db import models

class AbstractWord(models.Model):
     word = models.CharField(max_length=128, null=True)