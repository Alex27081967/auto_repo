"""
login_page.py

Страница авторизации.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        """
        Инициализация страницы.

        Args:
            driver (webdriver.Chrome): WebDriver.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username: str, password: str) -> None:
        """
        Вводит логин и пароль, нажимает кнопку входа.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль.

        Returns:
            None
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

        # Ожидаем загрузки следующей страницы
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
