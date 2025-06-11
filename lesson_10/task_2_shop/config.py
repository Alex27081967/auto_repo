"""
config.py

Конфигурационные данные для автотестов интернет-магазина SauceDemo.

Содержит базовый URL, данные для логина, информацию покупателя и ожидаемую сумму заказа.
"""

# URL интернет-магазина
BASE_URL = "https://www.saucedemo.com/"

# Учетные данные пользователя для авторизации
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Информация для оформления заказа
FIRST_NAME = "Ivan"
LAST_NAME = "Ivanov"
POSTAL_CODE = "12345"

# Ожидаемая итоговая сумма заказа (пример)
EXPECTED_TOTAL = "$58.29"
