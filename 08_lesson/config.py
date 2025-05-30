# 08_lesson/config.py

from auth_client import AuthClient

# Получаем токен и URL через авторизационный клиент
auth = AuthClient()
BASE_URL = auth.base_url
AUTH_TOKEN = auth.get_token()

# Заголовки по умолчанию для всех API-запросов
HEADERS = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json; charset=utf-8",
}
