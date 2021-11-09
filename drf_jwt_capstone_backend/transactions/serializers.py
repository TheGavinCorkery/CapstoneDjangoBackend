from rest_framework import serializers
from .models import Transaction, CategoryTotal, LedgerTotal

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'ledger', 'date', 'place', 'total',
        'description', 'category', 'user']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['ledger_id', 'category', 'total']

class LedgerTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTotal
        fields = ['ledger_id', 'ledger_name', 'total']
        
class LedgerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerTotal
        fields = ['category', 'total']