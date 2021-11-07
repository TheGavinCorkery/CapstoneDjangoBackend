from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'ledger', 'date', 'place', 'total',
        'description', 'category', 'user']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['ledger_id', 'category', 'total']