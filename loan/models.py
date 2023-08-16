from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.exceptions import ValidationError


class User(AbstractUser):
    Provider = "PR"
    Customer = "CT"
    Bank_personnel = "BP"
    YEAR_IN_SCHOOL_CHOICES = [
        (Provider, "Provider"),
        (Customer, "Customer"),
        (Bank_personnel, "Bank_personnel"),
    ]
    type = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=Customer,
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )

    def __str__(self):
        return f"{self.uuid}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"


class Bank_personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    total_budget = models.IntegerField(default=0)

    bank_personnel = models.ForeignKey(
        Bank_personnel, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.name}"


class Loan(models.Model):
    total_amount = models.IntegerField(null=True, blank=True)
    # total_money = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    max_duration = models.IntegerField()
    interest_rate = models.IntegerField()
    status = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    DisplayFields =['total_amount','duration','min_amount','max_amount','max_duration','interest_rate','status','start_date']

    coustmer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True
    )
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    bank_personnel = models.ForeignKey(Bank_personnel, on_delete=models.CASCADE)

    @property
    def total_money(self):
        if self.total_amount is not None:
            total_money = 0

            total_money = self.total_amount * self.interest_rate
            total_money= total_money * self.duration
            return total_money

    def clean(self):
        if self.max_amount < self.min_amount:
            raise ValidationError("min_amount fields bigger than max_amount")
        x = 0

        for e in self.provider.loan_set.all():
            if e.total_amount is not None:
                x = x + e.total_amount

        if x > self.provider.total_budget:
            raise ValidationError(
                "total of max_amount of loans fields bigger than total_budget of the provider"
            )

        if self.provider.total_budget < self.max_amount:
            raise ValidationError(
                "max_amount fields bigger than total_budget of the provider"
            )
        if self.duration is not None:
            if self.max_duration < self.duration:
                raise ValidationError("duration field bigger than max_duration")
        if self.total_amount is not None:
            if self.total_amount < self.min_amount:
                raise ValidationError("min_amount fields bigger than total_amount")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Payment(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def clean(self):
        for e in self.loan_set.payment.all():
            if e.total_amount is not None:
                x = x + e.total_amount
        if x > self.loan.total_budget:
            raise ValidationError(
                "total of max_amount of loans fields bigger than total_budget of the provider"
            )
