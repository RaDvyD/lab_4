# urls.py (веб-інтерфейс)

from django.urls import path
from . import views  # Підключаємо тільки views

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка

    # Веб-інтерфейс для Clients
    path('clients/', views.clients_list, name='clients_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('clients/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),

    # Веб-інтерфейс для Employees
    path('employees/', views.employees_list, name='employees_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),

    # Веб-інтерфейс для Pawned Items
    path('pawned_items/', views.pawned_items_list, name='pawned_items_list'),
    path('pawned_items/add/', views.add_pawned_item, name='add_pawned_item'),
    path('pawned_items/<int:item_id>/', views.pawned_item_detail, name='pawned_item_detail'),
    path('pawned_items/<int:item_id>/edit/', views.edit_pawned_item, name='edit_pawned_item'),
    path('pawned_items/<int:item_id>/delete/', views.delete_pawned_item, name='delete_pawned_item'),

    # Веб-інтерфейс для Loans
    path('loans/', views.loans_list, name='loans_list'),
    path('loans/add/', views.add_loan, name='add_loan'),
    path('loans/<int:loan_id>/', views.loan_detail, name='loan_detail'),
    path('loans/<int:loan_id>/edit/', views.edit_loan, name='edit_loan'),
    path('loans/<int:loan_id>/delete/', views.delete_loan, name='delete_loan'),

    # Веб-інтерфейс для Transactions
    path('transactions/', views.transactions_list, name='transactions_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/<int:transaction_id>/edit/', views.edit_transaction, name='edit_transaction'),
    path('transactions/<int:transaction_id>/delete/', views.delete_transaction, name='delete_transaction'),

    # Дашборди
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_bokeh/', views.dashboard_bokeh, name='dashboard_bokeh'),
    path('dashboard_performance/', views.dashboard_performance, name='dashboard_performance'),



    # Error Pages
    path('404/', views.custom_page_not_found_view, name='page_not_found'),
    path('500/', views.custom_error_view, name='server_error'),
]