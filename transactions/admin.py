from django.contrib import admin

# Register your models here.
from transactions.models import IncomeTransaction, SpendingTransaction


class IncomeTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_wallet', 'income', 'amount', 'transaction_date',)
    list_filter = ('user', 'transaction_date',)
    using = 'mongodb'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super(IncomeTransactionAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class SpendingTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'from_wallet', 'spending', 'amount', 'transaction_date',)
    list_filter = ('user', 'transaction_date',)
    using = 'mongodb'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super(SpendingTransactionAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


admin.site.register(IncomeTransaction, IncomeTransactionAdmin)
admin.site.register(SpendingTransaction, SpendingTransactionAdmin)
