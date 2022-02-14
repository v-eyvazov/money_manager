from django.urls import path, include


from money_manager_api import views

urlpatterns = [
    path('wallets', views.get_wallets, name="wallets"),
    path('create-wallet', views.create_wallet, name="create-wallet"),
    path('remove-wallet', views.remove_wallet, name="remove-wallet"),
    path('transfer', views.transfer, name="transfer"),
    path('income', views.get_income, name="income"),
    path('create-income', views.create_income, name="create-income"),
    path('remove-income', views.remove_income, name="remove-income"),




    path('transactions/', include('transactions_mongo.urls'))
]