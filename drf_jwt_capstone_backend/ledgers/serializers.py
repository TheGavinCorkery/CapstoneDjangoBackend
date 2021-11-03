from rest_framework import serializers
from .models import Ledger

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['id', 'user_id', 'name', 'total']