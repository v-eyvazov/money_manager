from rest_framework import serializers
from .models import IncomeTransaction, SpendingTransaction


class IncomeTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTransaction
        fields = ['_id', 'user', 'to_wallet', 'income', 'amount', 'transaction_date']


class SpendingTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingTransaction
        fields = ['_id', 'user', 'from_wallet', 'spending', 'amount', 'transaction_date']
