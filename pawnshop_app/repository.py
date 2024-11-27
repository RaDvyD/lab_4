# repository.py

from django.db.models import Avg, Sum, Count, Min, Max
from django.db.models.functions import TruncMonth, ExtractYear
from django.core.exceptions import ObjectDoesNotExist
from .models import Client, Employee, PawnedItem, Loan, Transaction


class BaseRepository:
    """Базовий репозиторій для CRUD операцій."""

    def __init__(self, model):
        self.model = model

    def get_all(self):

        return self.model.objects.all()
    def count(self):

        return self.model.objects.count

    def get_by_id(self, obj_id):

        try:
            return self.model.objects.get(id=obj_id)
        except ObjectDoesNotExist:
            return None

    def create(self, **kwargs):

        return self.model.objects.create(**kwargs)

    def update(self, obj_id, **kwargs):

        instance = self.get_by_id(obj_id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            instance.save()
        return instance

    def delete(self, obj_id):

        instance = self.get_by_id(obj_id)
        if instance:
            instance.delete()
        return instance


class LoanRepository(BaseRepository):


    def __init__(self):
        super().__init__(Loan)

    def average_loan_amount_per_month(self):
        loans = self.model.objects.annotate(month=TruncMonth('start_date'))
        loans_grouped = loans.values('month').annotate(avg_loan=Avg('loan_amount')).order_by('month')
        return loans_grouped

    def loans_count_by_interest_rate(self):
        loans_grouped = self.model.objects.values('interest_rate').annotate(total_loans=Count('id')).order_by(
            'interest_rate')
        return loans_grouped

    def min_max_loan_amount_per_client(self):
        loans_grouped = self.model.objects.values('client__name', 'client__surname').annotate(
            min_loan=Min('loan_amount'),
            max_loan=Max('loan_amount')
        ).order_by('client__name', 'client__surname')
        return loans_grouped

    def total_loans_per_year(self):
        loans = self.model.objects.annotate(year=ExtractYear('start_date'))
        loans_grouped = loans.values('year').annotate(total_loans=Count('id')).order_by('year')
        return loans_grouped


class PawnedItemRepository(BaseRepository):

    def __init__(self):
        super().__init__(PawnedItem)

    def total_pawned_items_by_client(self, client_name=None, client_surname=None):

        items_grouped = self.model.objects.values('client__name', 'client__surname')

        if client_name and client_surname:
            items_grouped = items_grouped.filter(client__name=client_name, client__surname=client_surname)

        items_grouped = items_grouped.annotate(total_items=Count('id')).order_by('-total_items')
        return items_grouped


class TransactionRepository(BaseRepository):

    def __init__(self):
        super().__init__(Transaction)

    def total_transactions_by_employee(self):
        transactions_grouped = self.model.objects.values('employee__name').annotate(
            total_amount=Sum('amount')).order_by('-total_amount')
        return transactions_grouped


class ClientRepository(BaseRepository):


    def __init__(self):
        super().__init__(Client)


class EmployeeRepository(BaseRepository):


    def __init__(self):
        super().__init__(Employee)


class Repository:
    """Єдина точка доступу до всіх репозиторіїв та їх методів."""

    Clients = ClientRepository()
    Employees = EmployeeRepository()
    PawnedItems = PawnedItemRepository()
    Loans = LoanRepository()
    Transactions = TransactionRepository()