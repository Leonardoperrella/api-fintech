from django.db import models
from django.utils import timezone


class Loans(models.Model):
    amount = models.FloatField()
    term = models.PositiveIntegerField()
    rate = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def installments(self):
        r = self.rate/12
        return (r + r / (((1 + r) ** self.term) - 1)) * self.amount


class Payments(models.Model):
    loan = models.ForeignKey(Loans, on_delete='PROTECT')
    paid = models.TextField(choices=(('made', 'made'), ('missed', 'missed')))
    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now)


class Balance(models.Model):
    class Meta:
        abstract = True

    def balance(self):
        payments = Payments.objects.filter(loan_id=self.id, paid='made')
        return self.amount - sum([pay.amount for pay in payments])
