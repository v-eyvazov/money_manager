from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from user_account.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
