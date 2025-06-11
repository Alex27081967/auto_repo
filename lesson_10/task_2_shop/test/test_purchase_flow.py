"""
test_purchase_flow.py

Тест проверяет полный сценарий покупки товаров на сайте https://www.saucedemo.com/
с использованием Page Object модели и аннотаций Allure для генерации отчёта.
"""

import allure
import pytest
from config import (
    BASE_URL,
    USERNAME,
    PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    EXPECTED_TOTAL,
)
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Покупка товара")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный сценарий покупки товара")
@allure.description(
    "Тест авторизуется, добавляет товары в корзину, проходит оформление и завершает заказ."
)
@pytest.mark.smoke
def test_complete_purchase_flow(driver):
    with allure.step("Открываем сайт и проверяем заголовок"):
        driver.get(BASE_URL)
        assert "Swag Labs" in driver.title, "Не удалось открыть сайт SauceDemo"

    with allure.step("Инициализируем страницы"):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

    with allure.step("Выполняем вход в систему"):
        login_page.login(USERNAME, PASSWORD)

    with allure.step("Добавляем товары в корзину"):
        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()

    with allure.step("Переходим в корзину и проверяем количество товаров"):
        inventory_page.go_to_cart()
        items_count = cart_page.get_cart_items_count()
        assert items_count == 3, f"Ожидалось 3 товара, но найдено {items_count}"

    with allure.step("Переходим к оформлению заказа и вводим данные"):
        cart_page.click_checkout()
        checkout_page.fill_customer_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    with allure.step("Проверяем итоговую сумму заказа"):
        total = checkout_page.get_total_price()
        assert (
                total == EXPECTED_TOTAL
        ), f"Ожидалась сумма {EXPECTED_TOTAL}, но получено {total}"

    with allure.step("Завершаем оформление заказа"):
        checkout_page.finish_order()
        assert checkout_page.is_order_complete(), "Заказ не завершен успешно"
