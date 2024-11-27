# api_urls.py

from django.urls import path
from . import api_views  # Підключаємо тільки api_views, оскільки це файл для API

urlpatterns = [
    # API для Clients
    path('clients/', api_views.ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', api_views.ClientDetail.as_view(), name='client-detail'),

    # API для Employees
    path('employees/', api_views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', api_views.EmployeeDetail.as_view(), name='employee-detail'),

    # API для Pawned Items
    path('pawned-items/', api_views.PawnedItemList.as_view(), name='pawneditem-list'),
    path('pawned-items/<int:pk>/', api_views.PawnedItemDetail.as_view(), name='pawneditem-detail'),

    # API для Loans
    path('loans/', api_views.LoanList.as_view(), name='loan-list'),
    path('loans/<int:pk>/', api_views.LoanDetail.as_view(), name='loan-detail'),

    # API для Transactions
    path('transactions/', api_views.TransactionList.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', api_views.TransactionDetail.as_view(), name='transaction-detail'),

    # Агреговані звіти API
    path('report/', api_views.AggregatedReport.as_view(), name='aggregated-report'),

    path('analytics/average-loan-amount-per-month/', api_views.AverageLoanAmountPerMonth.as_view(),
         name='average-loan-amount-per-month'),
    path('analytics/total-pawned-items-by-client/', api_views.TotalPawnedItemsByClient.as_view(),
         name='total-pawned-items-by-client'),
    path('analytics/total-transactions-by-employee/', api_views.TotalTransactionsByEmployee.as_view(),
         name='total-transactions-by-employee'),
    path('analytics/loans-count-by-interest-rate/', api_views.LoansCountByInterestRate.as_view(),
         name='loans-count-by-interest-rate'),
    path('analytics/min-max-loan-amount-per-client/', api_views.MinMaxLoanAmountPerClient.as_view(),
         name='min-max-loan-amount-per-client'),
    path('analytics/total-loans-per-year/', api_views.TotalLoansPerYear.as_view(), name='total-loans-per-year'),
]
# Якщо потрібні додаткові статистики, додайте їх тут
# path('analytics/loan-amount-statistics/', api_views.LoanAmountStatistics.as_view(), name='loan-amount-statistics'),
# path('analytics/transaction-amount-statistics/', api_views.TransactionAmountStatistics.as_view(), name='transaction-amount-statistics'),
# path('analytics/pawneditem-value-statistics/', api_views.PawnedItemValueStatistics.as_view(), name='pawneditem-value-statistics'),