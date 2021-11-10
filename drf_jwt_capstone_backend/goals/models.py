from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Goal(models.Model):
    ledger = models.ForeignKey('ledgers.Ledger', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    goalAmount = models.FloatField()
    category = models.CharField(max_length=20)