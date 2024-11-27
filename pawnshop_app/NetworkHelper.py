import requests

class NetworkHelper:
    BASE_URL = "http://127.0.0.1:8000/api/"  # Заміни на реальний URL вашого API
    TOKEN = "777aced20de6ab58029ee1dfbb931878412c8965"  # Замініть на реальний токен
    HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {TOKEN}'
    }

    @staticmethod
    def get(endpoint):
        response = requests.get(f"{NetworkHelper.BASE_URL}{endpoint}", headers=NetworkHelper.HEADERS)
        return response.json() if response.status_code == 200 else None

    @staticmethod
    def post(endpoint, data):
        response = requests.post(f"{NetworkHelper.BASE_URL}{endpoint}", json=data, headers=NetworkHelper.HEADERS)
        return response.json() if response.status_code == 201 else None

    @staticmethod
    def put(endpoint, data):
        response = requests.put(f"{NetworkHelper.BASE_URL}{endpoint}", json=data, headers=NetworkHelper.HEADERS)
        return response.json() if response.status_code == 200 else None

    @staticmethod
    def delete(endpoint):
        response = requests.delete(f"{NetworkHelper.BASE_URL}{endpoint}", headers=NetworkHelper.HEADERS)
        return response.status_code == 204  # Повертає True, якщо видалення успішне
