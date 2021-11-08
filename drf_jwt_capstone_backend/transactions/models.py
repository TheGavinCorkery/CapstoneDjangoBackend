from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey
User = get_user_model()

# Create your models here.
class Transaction(models.Model):
    ledger = models.ForeignKey('ledgers.Ledger', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    date = models.DateField()
    place = models.CharField(max_length=40)
    total = models.FloatField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length= 20)

class CategoryTotal(models.Model):
    ledger_id = models.IntegerField()
    ledger_name = models.CharField(max_length=30)
    total = models.FloatField()