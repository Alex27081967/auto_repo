import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()


class AuthClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.company_name = os.getenv("COMPANY_NAME")

    def get_company_id(self):
        """
        Получение companyId по логину, паролю и названию компании.
        """
        url = f"{self.base_url}/api-v2/auth/companies"
        payload = {
            "login": self.login,
            "password": self.password,
            "name": self.company_name,
        }
        response = requests.post(url, json=payload)
        assert (
                response.status_code == 200
        ), f"Ошибка получения companyId: {response.text}"
        companies = response.json().get("content", [])
        assert companies, "Список компаний пуст"
        return companies[0]["id"]

    def get_token(self):
        """
        Получение токена через /api-v2/auth/keys.
        """
        company_id = self.get_company_id()
        url = f"{self.base_url}/api-v2/auth/keys"
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": company_id,
        }
        response = requests.post(url, json=payload)
        assert response.status_code == 201, f"Ошибка получения токена: {response.text}"
        return f"Bearer {response.json()['key']}"
