from rest_framework import serializers
from .models import Wallet, Income, Spending


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['wallet', 'amount']


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['income']


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spending
        fields = ['spending']
