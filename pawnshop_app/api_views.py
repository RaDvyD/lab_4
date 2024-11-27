# api_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .repository import Repository
from django.http import Http404
import pandas as pd



# Статистичний аналіз суми позик
class LoanAmountStatistics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Loans.get_all().values('loan_amount')
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)

        mean_value = df['loan_amount'].mean()
        median_value = df['loan_amount'].median()
        min_value = df['loan_amount'].min()
        max_value = df['loan_amount'].max()

        stats = {
            'mean': mean_value,
            'median': median_value,
            'min': min_value,
            'max': max_value
        }
        return Response(stats)


# Статистичний аналіз суми транзакцій
class TransactionAmountStatistics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Transactions.get_all().values('amount')
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)

        mean_value = df['amount'].mean()
        median_value = df['amount'].median()
        min_value = df['amount'].min()
        max_value = df['amount'].max()

        stats = {
            'mean': mean_value,
            'median': median_value,
            'min': min_value,
            'max': max_value
        }
        return Response(stats)


# Статистичний аналіз вартості предметів застави
class PawnedItemValueStatistics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.PawnedItems.get_all().values('value')
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)

        mean_value = df['value'].mean()
        median_value = df['value'].median()
        min_value = df['value'].min()
        max_value = df['value'].max()

        stats = {
            'mean': mean_value,
            'median': median_value,
            'min': min_value,
            'max': max_value
        }
        return Response(stats)


# Клієнти
class ClientList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Repository.Clients.get_all()
        client_data = [{"id": client.id, "name": client.name, "surname": client.surname} for client in clients]
        return Response(client_data)

    def post(self, request):
        data = request.data
        client = Repository.Clients.create(**data)
        return Response({"id": client.id, "name": client.name, "surname": client.surname}, status=status.HTTP_201_CREATED)


class ClientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        client = Repository.Clients.get_by_id(pk)
        if client is None:
            raise Http404
        return client

    def get(self, request, pk):
        client = self.get_object(pk)
        return Response({
            "id": client.id,
            "name": client.name,
            "surname": client.surname,
            "address": client.address,
            "phone_number": client.phone_number,
            "passport_number": client.passport_number,
        })

    def put(self, request, pk):
        client = self.get_object(pk)
        data = request.data
        updated_client = Repository.Clients.update(client.id, **data)
        return Response({
            "id": updated_client.id,
            "name": updated_client.name,
            "surname": updated_client.surname,
            "address": updated_client.address,
            "phone_number": updated_client.phone_number,
            "passport_number": updated_client.passport_number,
        })

    def delete(self, request, pk):
        client = self.get_object(pk)
        Repository.Clients.delete(client.id)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Співробітники
class EmployeeList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = Repository.Employees.get_all()
        employee_data = [{"id": emp.id, "name": emp.name, "position": emp.position} for emp in employees]
        return Response(employee_data)

    def post(self, request):
        data = request.data
        employee = Repository.Employees.create(**data)
        return Response({"id": employee.id, "name": employee.name, "position": employee.position}, status=status.HTTP_201_CREATED)


class EmployeeDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        employee = Repository.Employees.get_by_id(pk)
        if employee is None:
            raise Http404
        return employee

    def get(self, request, pk):
        employee = self.get_object(pk)
        return Response({
            "id": employee.id,
            "name": employee.name,
            "position": employee.position,
            "phone_number": employee.phone_number,
        })

    def put(self, request, pk):
        employee = self.get_object(pk)
        data = request.data
        updated_employee = Repository.Employees.update(employee.id, **data)
        return Response({
            "id": updated_employee.id,
            "name": updated_employee.name,
            "position": updated_employee.position,
            "phone_number": updated_employee.phone_number,
        })

    def delete(self, request, pk):
        employee = self.get_object(pk)
        Repository.Employees.delete(employee.id)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Предмети застави
class PawnedItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Repository.PawnedItems.get_all()
        item_data = [{"id": item.id, "item_name": item.item_name, "description": item.description} for item in items]
        return Response(item_data)

    def post(self, request):
        data = request.data
        item = Repository.PawnedItems.create(**data)
        return Response({"id": item.id, "item_name": item.item_name, "description": item.description}, status=status.HTTP_201_CREATED)


class PawnedItemDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        item = Repository.PawnedItems.get_by_id(pk)
        if item is None:
            raise Http404
        return item

    def get(self, request, pk):
        item = self.get_object(pk)
        client = Repository.Clients.get_by_id(item.client.id) if item.client else None
        return Response({
            "id": item.id,
            "item_name": item.item_name,
            "description": item.description,
            "value": item.value,
            "pawn_date": item.pawn_date,
            "client": {
                "id": client.id,
                "name": client.name,
                "surname": client.surname
            } if client else None
        })

    def put(self, request, pk):
        item = self.get_object(pk)
        data = request.data
        updated_item = Repository.PawnedItems.update(item.id, **data)
        return Response({
            "id": updated_item.id,
            "item_name": updated_item.item_name,
            "description": updated_item.description,
            "value": updated_item.value,
            "pawn_date": updated_item.pawn_date,
            "client_id": updated_item.client.id
        })

    def delete(self, request, pk):
        item = self.get_object(pk)
        Repository.PawnedItems.delete(item.id)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Позики
class LoanList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        loans = Repository.Loans.get_all()
        loan_data = [{"id": loan.id, "client": loan.client.id, "amount": loan.loan_amount} for loan in loans]
        return Response(loan_data)

    def post(self, request):
        data = request.data
        loan = Repository.Loans.create(**data)
        return Response({"id": loan.id, "client": loan.client.id, "amount": loan.loan_amount}, status=status.HTTP_201_CREATED)


class LoanDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        loan = Repository.Loans.get_by_id(pk)
        if loan is None:
            raise Http404
        return loan

    def get(self, request, pk):
        loan = self.get_object(pk)
        client = Repository.Clients.get_by_id(loan.client.id) if loan.client else None
        item = Repository.PawnedItems.get_by_id(loan.item.id) if loan.item else None
        return Response({
            "id": loan.id,
            "client": {
                "id": client.id,
                "name": client.name,
                "surname": client.surname
            } if client else None,
            "item": {
                "id": item.id,
                "item_name": item.item_name
            } if item else None,
            "loan_amount": loan.loan_amount,
            "interest_rate": loan.interest_rate,
            "start_date": loan.start_date,
            "end_date": loan.end_date,
        })

    def put(self, request, pk):
        loan = self.get_object(pk)
        data = request.data
        updated_loan = Repository.Loans.update(loan.id, **data)
        return Response({
            "id": updated_loan.id,
            "client_id": updated_loan.client.id,
            "item_id": updated_loan.item.id,
            "loan_amount": updated_loan.loan_amount,
            "interest_rate": updated_loan.interest_rate,
            "start_date": updated_loan.start_date,
            "end_date": updated_loan.end_date,
        })

    def delete(self, request, pk):
        loan = self.get_object(pk)
        Repository.Loans.delete(loan.id)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Транзакції
class TransactionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Repository.Transactions.get_all()
        transaction_data = [{"id": transaction.id, "loan": transaction.loan.id, "amount": transaction.amount} for transaction in transactions]
        return Response(transaction_data)

    def post(self, request):
        data = request.data
        transaction = Repository.Transactions.create(**data)
        return Response({"id": transaction.id, "loan": transaction.loan.id, "amount": transaction.amount}, status=status.HTTP_201_CREATED)


class TransactionDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        transaction = Repository.Transactions.get_by_id(pk)
        if transaction is None:
            raise Http404
        return transaction

    def get(self, request, pk):
        transaction = self.get_object(pk)
        loan = Repository.Loans.get_by_id(transaction.loan.id) if transaction.loan else None
        employee = Repository.Employees.get_by_id(transaction.employee.id) if transaction.employee else None
        return Response({
            "id": transaction.id,
            "loan": {
                "id": loan.id,
                "loan_amount": loan.loan_amount
            } if loan else None,
            "employee": {
                "id": employee.id,
                "name": employee.name
            } if employee else None,
            "transaction_date": transaction.transaction_date,
            "amount": transaction.amount,
        })

    def put(self, request, pk):
        transaction = self.get_object(pk)
        data = request.data
        updated_transaction = Repository.Transactions.update(transaction.id, **data)
        return Response({
            "id": updated_transaction.id,
            "loan_id": updated_transaction.loan.id,
            "employee_id": updated_transaction.employee.id,
            "transaction_date": updated_transaction.transaction_date,
            "amount": updated_transaction.amount,
        })

    def delete(self, request, pk):
        transaction = self.get_object(pk)
        Repository.Transactions.delete(transaction.id)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Агрегований звіт
class AggregatedReport(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_loans = Repository.Loans.count()
        total_clients = Repository.Clients.count()
        total_items = Repository.PawnedItems.count()

        data = {
            "total_loans": total_loans,
            "total_clients": total_clients,
            "total_items": total_items,
        }
        return Response(data, status=status.HTTP_200_OK)


# Агреговані звіти

class AverageLoanAmountPerMonth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Loans.average_loan_amount_per_month()
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)
        df['month'] = pd.to_datetime(df['month']).dt.strftime('%Y-%m')
        return Response(df.to_dict(orient='records'))


class TotalPawnedItemsByClient(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.PawnedItems.total_pawned_items_by_client()
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)
        return Response(df.to_dict(orient='records'))


class TotalTransactionsByEmployee(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Transactions.total_transactions_by_employee()
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)
        return Response(df.to_dict(orient='records'))


class LoansCountByInterestRate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Loans.loans_count_by_interest_rate()
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)
        return Response(df.to_dict(orient='records'))


class MinMaxLoanAmountPerClient(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Loans.min_max_loan_amount_per_client()
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)
        return Response(df.to_dict(orient='records'))


class TotalLoansPerYear(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Repository.Loans.total_loans_per_year()
        df = pd.DataFrame(list(data))
        if df.empty:
            return Response({"detail": "Немає даних для аналізу."}, status=status.HTTP_200_OK)
        return Response(df.to_dict(orient='records'))