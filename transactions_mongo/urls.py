from django.urls import path
from transactions_mongo import views

urlpatterns = [
    path('income-transactions', views.get_income_transactions, name="income-transactions"),
    path('create-income-transaction', views.create_income_transaction, name="create-income-transaction"),
    path('remove-income-transaction', views.remove_income_transaction, name="remove-income-transaction"),

    path('spending-transactions', views.get_spending_transactions, name="spending-transactions"),
    path('create-spending-transaction', views.create_spending_transaction, name="create-spending-transaction"),
    path('remove-spending-transaction', views.remove_spending_transaction, name="remove-spending-transaction")
]
