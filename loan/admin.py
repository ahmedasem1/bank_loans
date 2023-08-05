from django.contrib import admin
from .models import User, Provider, Customer, Bank_personnel, Loan, Payment

admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Payment)


admin.site.register(Bank_personnel)
