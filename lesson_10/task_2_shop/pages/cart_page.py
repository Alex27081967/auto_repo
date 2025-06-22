"""
cart_page.py

Страница корзины.
"""

from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы.

        Args:
            driver (webdriver.Chrome): WebDriver.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        Returns:
            None
        """
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.

        Returns:
            int: Количество товаров.
        """
        return len(self.driver.find_elements(*self.cart_items))
