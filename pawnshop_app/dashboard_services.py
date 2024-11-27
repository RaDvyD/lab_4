import requests
import pandas as pd
from django.conf import settings
import time
import psutil
import concurrent.futures


class DashboardService:
    def __init__(self):
        self.api_base_url = settings.API_BASE_URL
        self.headers = {'Authorization': f'Token {settings.API_TOKEN}'}

    def get_average_loan_amount_per_month(self, selected_year=None):
        try:
            params = {}
            if selected_year:
                params['year'] = selected_year
            response = requests.get(f'{self.api_base_url}analytics/average-loan-amount-per-month/', headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            if df.empty:
                return {"error": "Немає даних для середньої суми позики за місяць."}
            df['month'] = pd.to_datetime(df['month']).dt.strftime('%Y-%m')
            return df
        except requests.exceptions.RequestException:
            return {"error": "Сталася помилка при завантаженні даних для середньої суми позики за місяць."}

    def get_total_pawned_items_by_client(self, selected_client=None):
        try:
            params = {}
            if selected_client:
                params['client'] = selected_client
            response = requests.get(f'{self.api_base_url}analytics/total-pawned-items-by-client/', headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            if df.empty:
                return {"error": "Немає даних для кількості предметів застави за клієнтами."}
            return df
        except requests.exceptions.RequestException:
            return {"error": "Сталася помилка при завантаженні даних для кількості предметів застави за клієнтами."}

    def get_loans_count_by_interest_rate(self):
        try:
            response = requests.get(f'{self.api_base_url}analytics/loans-count-by-interest-rate/', headers=self.headers)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            if df.empty:
                return {"error": "Немає даних для кількості позик за відсотковими ставками."}
            return df
        except requests.exceptions.RequestException:
            return {"error": "Сталася помилка при завантаженні даних для кількості позик за відсотковими ставками."}

    def get_min_max_loan_amount_per_client(self):
        try:
            response = requests.get(f'{self.api_base_url}analytics/min-max-loan-amount-per-client/', headers=self.headers)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            if df.empty:
                return {"error": "Немає даних для мінімальної та максимальної суми позики для кожного клієнта."}
            return df
        except requests.exceptions.RequestException:
            return {"error": "Сталася помилка при завантаженні даних для мінімальної та максимальної суми позики для кожного клієнта."}

    def get_total_loans_per_year(self):
        try:
            response = requests.get(f'{self.api_base_url}analytics/total-loans-per-year/', headers=self.headers)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            if df.empty:
                return {"error": "Немає даних для загальної кількості позик за роками."}
            return df
        except requests.exceptions.RequestException:
            return {"error": "Сталася помилка при завантаженні даних для загальної кількості позик за роками."}

    def get_total_transactions_by_employee(self):
        try:
            response = requests.get(f'{self.api_base_url}analytics/total-transactions-by-employee/', headers=self.headers)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            if df.empty:
                return {"error": "Немає даних для загальної суми транзакцій за співробітниками."}
            return df
        except requests.exceptions.RequestException:
            return {"error": "Сталася помилка при завантаженні даних для загальної суми транзакцій за співробітниками."}

    def get_performance_metrics(self, num_requests=100, thread_counts=None):
        if thread_counts is None:
            thread_counts = [1, 2, 4, 8, 16]

        def perform_query():
            start_time = time.time()
            requests.get(f'{self.api_base_url}loans/', headers=self.headers)
            end_time = time.time()
            return end_time - start_time

        def run_parallel_queries(num_threads):
            cpu_percent_before = psutil.cpu_percent(interval=None)
            mem_before = psutil.virtual_memory().percent

            with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = [executor.submit(perform_query) for _ in range(num_requests)]
                execution_times = [future.result() for future in concurrent.futures.as_completed(futures)]

            cpu_percent_after = psutil.cpu_percent(interval=None)
            mem_after = psutil.virtual_memory().percent

            avg_time_local = sum(execution_times) / len(execution_times) if execution_times else 0
            cpu_usage_local = cpu_percent_after - cpu_percent_before
            mem_usage_local = mem_after - mem_before

            return avg_time_local, cpu_usage_local, mem_usage_local

        performance_data = []
        for threads in thread_counts:
            avg_time_local, cpu_usage_local, mem_usage_local = run_parallel_queries(threads)
            performance_data.append({
                'threads': threads,
                'avg_time': avg_time_local,
                'cpu_usage': cpu_usage_local,
                'mem_usage': mem_usage_local,
            })

        return pd.DataFrame(performance_data)
