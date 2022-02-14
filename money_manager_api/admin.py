from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from money_manager_api.models import Person, Wallet, Income


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user_name',)


class WalletAdmin(admin.ModelAdmin):
    list_display = ('get_person', 'wallet', 'amount',)
    list_filter = ('person__user_name', 'wallet',)

    @display(ordering='wallet__person', description='Person')
    def get_person(self, obj):
        return obj.person.user_name


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('get_person', 'income',)
    list_filter = ('person__user_name', 'income',)

    @display(ordering='income__person', description='Person')
    def get_person(self, obj):
        return obj.person.user_name


admin.site.register(Person, PersonAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Income, IncomeAdmin)
