from rest_framework import serializers
from .models import IncomeTransaction


class IncomeTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTransaction
        fields = ['_id', 'user', 'to_wallet', 'income', 'amount', 'transaction_date']
