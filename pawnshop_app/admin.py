from django.contrib import admin
from .models import Client, Employee, PawnedItem, Loan, Transaction

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(PawnedItem)
admin.site.register(Loan)
admin.site.register(Transaction)
