from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    Provider = 'PR'
    Customer = 'CT'
    Bank_personnel = 'BP'
    YEAR_IN_SCHOOL_CHOICES = [
        (Provider, 'Provider'),
        (Customer, 'Customer'),
        (Bank_personnel, 'Bank_personnel')
    ]
    type = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=Customer,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,unique=True)
    def __str__(self):
            return f"{self.uuid}"





class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    job=models.CharField(max_length=100,null=True)
    def __str__(self):
            return f"{self.name}"

class Bank_personnel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
            return f"{self.name}"

class Provider(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    total_budget=models.IntegerField(default=0)
      
    bank_personnel=models.ForeignKey(Bank_personnel, on_delete=models.CASCADE,null=True)

    def __str__(self):
            return f"{self.name}"      
class payment(models.Model):
    amount=models.IntegerField()
    date=models.DateField()
    # sender=models.ForeignKey(User, on_delete=models.CASCADE)
    # receiver=models.ForeignKey(User, on_delete=models.CASCADE)



class Loan(models.Model):
    start_date=models.DateField(null=True)
    total_amount=models.IntegerField(null=True)
    duration=models.IntegerField(null=True)
    min_amount=models.IntegerField()      
    max_amount=models.IntegerField()    
    max_duration=models.IntegerField()   
    interest_rate=models.IntegerField()

    coustmer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    provider=models.ForeignKey(Provider, on_delete=models.CASCADE)
    bank_personnel=models.ForeignKey(Bank_personnel, on_delete=models.CASCADE)

      
    @property
    def interst_rate(self):
        return  (float(self.total_amount)*self.interest_rate)*self.duration

    # def get_discount(self):
    #     return "122"