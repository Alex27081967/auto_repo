"""
conftest.py

Общий конфиг для pytest, фикстуры.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для запуска и закрытия браузера Chrome.

    Возвращает:
        webdriver.Chrome - объект драйвера.
    """
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"]
    )
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.quit()
