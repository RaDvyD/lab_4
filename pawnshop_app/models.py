from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    passport_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class PawnedItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    pawn_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='pawned_items')

    def __str__(self):
        return self.item_name

class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(PawnedItem, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Loan {self.id} for {self.client}'

class Transaction(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transaction {self.id} for {self.loan.client} by {self.employee}'
