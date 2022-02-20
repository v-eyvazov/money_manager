from djongo import models


# Create your models here.
class IncomeTransaction(models.Model):
    _id = models.ObjectIdField()  # noqa
    user = models.CharField(max_length=20)
    to_wallet = models.CharField(max_length=50)
    income = models.CharField(max_length=50)
    amount = models.FloatField()
    transaction_date = models.DateField(auto_now=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.income} ({self.amount}) at {self.transaction_date}"


class SpendingTransaction(models.Model):
    _id = models.ObjectIdField()  # noqa
    user = models.CharField(max_length=20)
    from_wallet = models.CharField(max_length=50)
    spending = models.CharField(max_length=50)
    amount = models.FloatField()
    transaction_date = models.DateField(auto_now=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.spending} ({self.amount}) at {self.transaction_date}"
