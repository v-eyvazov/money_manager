from django.urls import path
from transactions_mongo import views

urlpatterns = [
    path('income-transactions', views.get_income_transactions, name="income-transactions"),
    path('create-income-transaction', views.create_income_transaction, name="create-income-transaction"),
    path('remove-income-transaction', views.remove_income_transaction, name="remove-income-transaction")
]
