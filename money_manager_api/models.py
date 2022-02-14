from django.db import models

# Create your models here.
from django.db.models import PROTECT


class Person(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name


class Wallet(models.Model):
    person = models.ForeignKey(Person, on_delete=PROTECT)  # One to Many
    wallet = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.person.user_name} {self.wallet}"


class Income(models.Model):
    person = models.ForeignKey(Person, on_delete=PROTECT)  # One to Many
    income = models.CharField(max_length=50)
    removed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Income"

    def __str__(self):
        return f"{self.person.user_name} {self.income}"
