'''


python manage.py runserver       # запуск сервера




python manage.py shell
from pawnshop_app.models import Client, Employee, PawnedItem, Loan, Transaction
from pawnshop_app.repository import Repository

Перевірка всіх клієнтів:

clients = Client.objects.all()
for client in clients:
    print(client)

Перевірка всіх клієнтів:

clients = Client.objects.all()
for client in clients:
    print(client)
z
Перевірка всіх предметів (застав):

pawned_items = PawnedItem.objects.all()
for item in pawned_items:
    print(item)

Перевірка всіх позик:

loans = Loan.objects.all()
for loan in loans:
    print(loan)

Перевірка всіх транзакцій:

transactions = Transaction.objects.all()
for transaction in transactions:
    print(transaction)






'''
