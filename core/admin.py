from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from core.models import Wallet, Income, Spending


class WalletAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'wallet', 'amount',)
    list_filter = ('user__username', 'wallet',)

    @display(ordering='wallet__user', description='CustomUser')
    def get_user(self, obj):
        return obj.user.username


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'income',)
    list_filter = ('user__username', 'income',)

    @display(ordering='wallet__user', description='CustomUser')
    def get_user(self, obj):
        return obj.user.username


class SpendingAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'spending',)
    list_filter = ('user__username', 'spending')

    @display(ordering='wallet__user', description='CustomUser')
    def get_user(self, obj):
        return obj.user.username


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Spending, SpendingAdmin)
