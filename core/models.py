from django.db import models

# Create your models here.
from django.db.models import PROTECT
from django.conf import settings


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)  # One to Many
    wallet = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} {self.wallet}"  # noqa


class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)  # One to Many
    income = models.CharField(max_length=50)
    removed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Income"

    def __str__(self):
        return f"{self.user.username} {self.income}"  # noqa


class Spending(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)  # One to Many
    spending = models.CharField(max_length=50)
    removed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Spending"

    def __str__(self):
        return f"{self.user.username} {self.spending}"  # noqa
