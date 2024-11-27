# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseNotFound
from .NetworkHelper import NetworkHelper
import pandas as pd
import plotly.express as px
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN






from .dashboard_services import DashboardService

# Головна сторінка
def home(request):
    return render(request, 'home.html', {})


# Клієнти
def clients_list(request):
    clients = NetworkHelper.get('clients/')
    return render(request, 'clients.html', {'clients': clients})


def client_detail(request, client_id):
    client = NetworkHelper.get(f'clients/{client_id}/')
    if client is None:
        return HttpResponseNotFound('Клієнта не знайдено')
    return render(request, 'client_detail.html', {'client': client})


def add_client(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'address': request.POST.get('address'),
            'phone_number': request.POST.get('phone_number'),
            'passport_number': request.POST.get('passport_number'),
        }
        NetworkHelper.post('clients/', data)
        return redirect(reverse('clients_list'))
    else:
        return render(request, 'add_client.html')


def edit_client(request, client_id):
    client = NetworkHelper.get(f'clients/{client_id}/')
    if client is None:
        return HttpResponseNotFound('Клієнта не знайдено')
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'address': request.POST.get('address'),
            'phone_number': request.POST.get('phone_number'),
            'passport_number': request.POST.get('passport_number'),
        }
        NetworkHelper.put(f'clients/{client_id}/', data)
        return redirect(reverse('clients_list'))
    else:
        return render(request, 'edit_client.html', {'client': client})


def delete_client(request, client_id):
    NetworkHelper.delete(f'clients/{client_id}/')
    return redirect(reverse('clients_list'))


# Співробітники
def employees_list(request):
    employees = NetworkHelper.get('employees/')
    return render(request, 'employees.html', {'employees': employees})


def employee_detail(request, employee_id):
    employee = NetworkHelper.get(f'employees/{employee_id}/')
    if employee is None:
        return HttpResponseNotFound('Співробітника не знайдено')
    return render(request, 'employee_detail.html', {'employee': employee})


def add_employee(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'position': request.POST.get('position'),
            'phone_number': request.POST.get('phone_number'),
        }
        NetworkHelper.post('employees/', data)
        return redirect(reverse('employees_list'))
    else:
        return render(request, 'add_employee.html')


def edit_employee(request, employee_id):
    employee = NetworkHelper.get(f'employees/{employee_id}/')
    if employee is None:
        return HttpResponseNotFound('Співробітника не знайдено')
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'position': request.POST.get('position'),
            'phone_number': request.POST.get('phone_number'),
        }
        NetworkHelper.put(f'employees/{employee_id}/', data)
        return redirect(reverse('employees_list'))
    else:
        return render(request, 'edit_employee.html', {'employee': employee})


def delete_employee(request, employee_id):
    NetworkHelper.delete(f'employees/{employee_id}/')
    return redirect(reverse('employees_list'))


# Предмети застави
def pawned_items_list(request):
    items = NetworkHelper.get('pawned-items/')
    return render(request, 'pawned_items.html', {'items': items})


def pawned_item_detail(request, item_id):
    item = NetworkHelper.get(f'pawned-items/{item_id}/')
    if item is None:
        return HttpResponseNotFound('Предмет не знайдено')
    return render(request, 'pawned_item_detail.html', {'item': item})


def add_pawned_item(request):
    if request.method == 'POST':
        data = {
            'item_name': request.POST.get('item_name'),
            'description': request.POST.get('description'),
            'value': request.POST.get('value'),
            'pawn_date': request.POST.get('pawn_date'),
            'client_id': request.POST.get('client_id'),
        }
        NetworkHelper.post('pawned-items/', data)
        return redirect(reverse('pawned_items_list'))
    else:
        clients = NetworkHelper.get('clients/')
        return render(request, 'add_pawned_item.html', {'clients': clients})


def edit_pawned_item(request, item_id):
    item = NetworkHelper.get(f'pawned-items/{item_id}/')
    if item is None:
        return HttpResponseNotFound('Предмет не знайдено')
    if request.method == 'POST':
        data = {
            'item_name': request.POST.get('item_name'),
            'description': request.POST.get('description'),
            'value': request.POST.get('value'),
            'pawn_date': request.POST.get('pawn_date'),
            'client_id': request.POST.get('client_id'),
        }
        NetworkHelper.put(f'pawned-items/{item_id}/', data)
        return redirect(reverse('pawned_items_list'))
    else:
        clients = NetworkHelper.get('clients/')
        return render(request, 'edit_pawned_item.html', {'item': item, 'clients': clients})


def delete_pawned_item(request, item_id):
    NetworkHelper.delete(f'pawned-items/{item_id}/')
    return redirect(reverse('pawned_items_list'))


# Позики
def loans_list(request):
    loans = NetworkHelper.get('loans/')
    return render(request, 'loans.html', {'loans': loans})


def loan_detail(request, loan_id):
    loan = NetworkHelper.get(f'loans/{loan_id}/')
    if loan is None:
        return HttpResponseNotFound('Позики не знайдено')
    return render(request, 'loan_detail.html', {'loan': loan})


def add_loan(request):
    if request.method == 'POST':
        data = {
            'client_id': request.POST.get('client_id'),
            'item_id': request.POST.get('item_id'),
            'loan_amount': request.POST.get('loan_amount'),
            'interest_rate': request.POST.get('interest_rate'),
            'start_date': request.POST.get('start_date'),
            'end_date': request.POST.get('end_date'),
        }
        NetworkHelper.post('loans/', data)
        return redirect(reverse('loans_list'))
    else:
        clients = NetworkHelper.get('clients/')
        items = NetworkHelper.get('pawned-items/')
        return render(request, 'add_loan.html', {'clients': clients, 'items': items})


def edit_loan(request, loan_id):
    loan = NetworkHelper.get(f'loans/{loan_id}/')
    if loan is None:
        return HttpResponseNotFound('Позики не знайдено')
    if request.method == 'POST':
        data = {
            'client_id': request.POST.get('client_id'),
            'item_id': request.POST.get('item_id'),
            'loan_amount': request.POST.get('loan_amount'),
            'interest_rate': request.POST.get('interest_rate'),
            'start_date': request.POST.get('start_date'),
            'end_date': request.POST.get('end_date'),
        }
        NetworkHelper.put(f'loans/{loan_id}/', data)
        return redirect(reverse('loans_list'))
    else:
        clients = NetworkHelper.get('clients/')
        items = NetworkHelper.get('pawned-items/')
        return render(request, 'edit_loan.html', {'loan': loan, 'clients': clients, 'items': items})


def delete_loan(request, loan_id):
    NetworkHelper.delete(f'loans/{loan_id}/')
    return redirect(reverse('loans_list'))


# Транзакції
def transactions_list(request):
    transactions = NetworkHelper.get('transactions/')
    return render(request, 'transactions.html', {'transactions': transactions})


def transaction_detail(request, transaction_id):
    transaction = NetworkHelper.get(f'transactions/{transaction_id}/')
    if transaction is None:
        return HttpResponseNotFound('Транзакції не знайдено')
    return render(request, 'transaction_detail.html', {'transaction': transaction})


def add_transaction(request):
    if request.method == 'POST':
        data = {
            'loan_id': request.POST.get('loan_id'),
            'employee_id': request.POST.get('employee_id'),
            'transaction_date': request.POST.get('transaction_date'),
            'amount': request.POST.get('amount'),
        }
        NetworkHelper.post('transactions/', data)
        return redirect(reverse('transactions_list'))
    else:
        loans = NetworkHelper.get('loans/')
        employees = NetworkHelper.get('employees/')
        return render(request, 'add_transaction.html', {'loans': loans, 'employees': employees})


def edit_transaction(request, transaction_id):
    transaction = NetworkHelper.get(f'transactions/{transaction_id}/')
    if transaction is None:
        return HttpResponseNotFound('Транзакції не знайдено')
    if request.method == 'POST':
        data = {
            'loan_id': request.POST.get('loan_id'),
            'employee_id': request.POST.get('employee_id'),
            'transaction_date': request.POST.get('transaction_date'),
            'amount': request.POST.get('amount'),
        }
        NetworkHelper.put(f'transactions/{transaction_id}/', data)
        return redirect(reverse('transactions_list'))
    else:
        loans = NetworkHelper.get('loans/')
        employees = NetworkHelper.get('employees/')
        return render(request, 'edit_transaction.html', {'transaction': transaction, 'loans': loans, 'employees': employees})


def delete_transaction(request, transaction_id):
    NetworkHelper.delete(f'transactions/{transaction_id}/')
    return redirect(reverse('transactions_list'))


# Дашборд
def dashboard(request):
    dashboard_service = DashboardService()

    selected_year = request.GET.get('year')
    selected_client = request.GET.get('client')

    context = {'selected_year': selected_year, 'selected_client': selected_client}

    # 1. Середня сума позики за місяць
    avg_loan_data = dashboard_service.get_average_loan_amount_per_month(selected_year)
    if isinstance(avg_loan_data, pd.DataFrame):
        fig_avg_loan = px.line(avg_loan_data, x='month', y='avg_loan', title='Середня сума позики за місяць')
        context['graph_avg_loan'] = fig_avg_loan.to_html(full_html=False)
    else:
        context['graph_avg_loan'] = f"<p>{avg_loan_data['error']}</p>"

    # 2. Загальна кількість предметів застави за клієнтами
    items_data = dashboard_service.get_total_pawned_items_by_client(selected_client)
    if isinstance(items_data, pd.DataFrame):
        fig_items = px.bar(items_data, x='client__name', y='total_items', title='Кількість предметів застави за клієнтами')
        context['graph_items'] = fig_items.to_html(full_html=False)
    else:
        context['graph_items'] = f"<p>{items_data['error']}</p>"

    # 3. Кількість позик за відсотковими ставками
    interest_data = dashboard_service.get_loans_count_by_interest_rate()
    if isinstance(interest_data, pd.DataFrame):
        fig_interest = px.bar(interest_data, x='interest_rate', y='total_loans', title='Кількість позик за відсотковими ставками')
        context['graph_interest'] = fig_interest.to_html(full_html=False)
    else:
        context['graph_interest'] = f"<p>{interest_data['error']}</p>"

    # 4. Мінімальна та максимальна сума позики для кожного клієнта
    min_max_data = dashboard_service.get_min_max_loan_amount_per_client()
    if isinstance(min_max_data, pd.DataFrame):
        fig_min_max = px.bar(min_max_data, x='client__name', y=['min_loan', 'max_loan'], barmode='group',
                             title='Мін/Макс сума позики для кожного клієнта')
        context['graph_min_max'] = fig_min_max.to_html(full_html=False)
    else:
        context['graph_min_max'] = f"<p>{min_max_data['error']}</p>"

    # 5. Загальна кількість позик за роками
    loans_year_data = dashboard_service.get_total_loans_per_year()
    if isinstance(loans_year_data, pd.DataFrame):
        fig_loans_year = px.bar(loans_year_data, x='year', y='total_loans', title='Загальна кількість позик за роками')
        context['graph_loans_year'] = fig_loans_year.to_html(full_html=False)
    else:
        context['graph_loans_year'] = f"<p>{loans_year_data['error']}</p>"

    # 6. Загальна сума транзакцій за співробітниками
    transactions_data = dashboard_service.get_total_transactions_by_employee()
    if isinstance(transactions_data, pd.DataFrame):
        fig_transactions = px.pie(
            transactions_data,
            names='employee__name',
            values='total_amount',
            title='Розподіл загальної суми транзакцій за співробітниками'
        )
        context['graph_transactions'] = fig_transactions.to_html(full_html=False)
    else:
        context['graph_transactions'] = f"<p>{transactions_data['error']}</p>"

    return render(request, 'dashboard.html', context)

# Дашборд з Bokeh
def dashboard_bokeh(request):
    dashboard_service = DashboardService()

    selected_year = request.GET.get('year')
    selected_client = request.GET.get('client')

    context = {'selected_year': selected_year, 'selected_client': selected_client}

    # 1. Середня сума позики за місяць
    avg_loan_data = dashboard_service.get_average_loan_amount_per_month(selected_year)
    if isinstance(avg_loan_data, pd.DataFrame):
        avg_loan_data['month'] = pd.to_datetime(avg_loan_data['month'])
        p1 = figure(x_axis_type='datetime', title='Середня сума позики за місяць', height=350, width=800)
        p1.line(avg_loan_data['month'], avg_loan_data['avg_loan'], line_width=2)
        p1.circle(avg_loan_data['month'], avg_loan_data['avg_loan'], size=8)
        script1, div1 = components(p1)
        context['script1'] = script1
        context['div1'] = div1
    else:
        context['script1'], context['div1'] = "", f"<p>{avg_loan_data['error']}</p>"

    # 2. Загальна кількість предметів застави за клієнтами
    items_data = dashboard_service.get_total_pawned_items_by_client(selected_client)
    if isinstance(items_data, pd.DataFrame):
        p2 = figure(x_range=items_data['client__name'], title='Кількість предметів застави за клієнтами', height=350, width=800)
        p2.vbar(x=items_data['client__name'], top=items_data['total_items'], width=0.9)
        p2.xgrid.grid_line_color = None
        p2.y_range.start = 0
        script2, div2 = components(p2)
        context['script2'] = script2
        context['div2'] = div2
    else:
        context['script2'], context['div2'] = "", f"<p>{items_data['error']}</p>"

    # 3. Кількість позик за відсотковими ставками
    interest_data = dashboard_service.get_loans_count_by_interest_rate()
    if isinstance(interest_data, pd.DataFrame):
        p3 = figure(x_range=interest_data['interest_rate'].astype(str), title='Кількість позик за відсотковими ставками', height=350, width=800)
        p3.vbar(x=interest_data['interest_rate'].astype(str), top=interest_data['total_loans'], width=0.9)
        p3.xgrid.grid_line_color = None
        p3.y_range.start = 0
        script3, div3 = components(p3)
        context['script3'] = script3
        context['div3'] = div3
    else:
        context['script3'], context['div3'] = "", f"<p>{interest_data['error']}</p>"

    # 4. Мінімальна та максимальна сума позики для кожного клієнта
    min_max_data = dashboard_service.get_min_max_loan_amount_per_client()
    if isinstance(min_max_data, pd.DataFrame):
        p4 = figure(x_range=min_max_data['client__name'], title='Мін/Макс сума позики для кожного клієнта', height=350, width=800)
        p4.vbar(x=min_max_data['client__name'], top=min_max_data['min_loan'], width=0.4, color='blue', legend_label='Min Loan', muted_alpha=0.2)
        p4.vbar(x=min_max_data['client__name'], top=min_max_data['max_loan'], width=0.4, color='red', legend_label='Max Loan', muted_alpha=0.2)
        p4.xgrid.grid_line_color = None
        p4.y_range.start = 0
        p4.legend.click_policy = 'mute'
        script4, div4 = components(p4)
        context['script4'] = script4
        context['div4'] = div4
    else:
        context['script4'], context['div4'] = "", f"<p>{min_max_data['error']}</p>"

    # 5. Загальна кількість позик за роками
    loans_year_data = dashboard_service.get_total_loans_per_year()
    if isinstance(loans_year_data, pd.DataFrame):
        p5 = figure(x_range=loans_year_data['year'].astype(str), title='Загальна кількість позик за роками', height=350, width=800)
        p5.vbar(x=loans_year_data['year'].astype(str), top=loans_year_data['total_loans'], width=0.9)
        p5.xgrid.grid_line_color = None
        p5.y_range.start = 0
        script5, div5 = components(p5)
        context['script5'] = script5
        context['div5'] = div5
    else:
        context['script5'], context['div5'] = "", f"<p>{loans_year_data['error']}</p>"

        # 6. Загальна сума транзакцій за співробітниками
    transactions_data = dashboard_service.get_total_transactions_by_employee()
    if isinstance(transactions_data, pd.DataFrame):
        p6 = figure(x_range=transactions_data['employee__name'], title='Розподіл загальної суми транзакцій за співробітниками', height=350, width=800)
        p6.vbar(x=transactions_data['employee__name'], top=transactions_data['total_amount'], width=0.9)
        p6.xgrid.grid_line_color = None
        p6.y_range.start = 0
        script6, div6 = components(p6)
        context['script6'] = script6
        context['div6'] = div6

    context['resources'] = CDN.render()

    return render(request, 'dashboard_bokeh.html', context)

def dashboard_performance(request):
    dashboard_service = DashboardService()
    performance_data = dashboard_service.get_performance_metrics()

    if isinstance(performance_data, pd.DataFrame):
        fig_time = px.line(performance_data, x='threads', y='avg_time', title='Час виконання запитів')
        fig_cpu = px.line(performance_data, x='threads', y='cpu_usage', title='Використання CPU')
        fig_mem = px.line(performance_data, x='threads', y='mem_usage', title='Використання пам\'яті')

        context = {
            'graph_time': fig_time.to_html(full_html=False),
            'graph_cpu': fig_cpu.to_html(full_html=False),
            'graph_mem': fig_mem.to_html(full_html=False),
        }
    else:
        context = {
            'error': "Не вдалося отримати дані для метрик продуктивності."
        }

    return render(request, 'dashboard_performance.html', context)


def custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def custom_error_view(request):
    return render(request, '500.html', status=500)