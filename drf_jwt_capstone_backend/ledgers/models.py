from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.related import ForeignKey

User = get_user_model()

# Create your models here.
class Ledger(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    total = models.FloatField()