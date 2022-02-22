from django.urls import path, include
from user_account.views import registration_view, fetch_token, login_view, logout_view

urlpatterns = [
    path('register', registration_view, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('fetch-token', fetch_token, name='fetch-token'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout')
]
