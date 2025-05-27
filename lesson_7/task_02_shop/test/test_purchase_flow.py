import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def create_driver():
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
    return driver


def test_complete_purchase_flow():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Авторизация
        login_page.login("standard_user", "secret_sauce")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Добавление товаров
        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()
        inventory_page.go_to_cart()

        # Корзина
        assert "cart.html" in driver.current_url
        assert cart_page.get_cart_items_count() == 3
        cart_page.click_checkout()

        # Оформление
        checkout_page.fill_customer_info("Иван", "Петров", "123456")
        assert "checkout-step-two.html" in driver.current_url
        assert checkout_page.get_total_price() == "$58.29"

        # Завершение
        checkout_page.finish_order()
        assert checkout_page.is_order_complete()

    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        pytest.fail(f"Тест упал: {str(e)}")
    finally:
        driver.quit()
