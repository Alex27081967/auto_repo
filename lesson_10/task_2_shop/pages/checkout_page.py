"""
checkout_page.py

Страница оформления заказа.
"""

from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализация страницы.

        Args:
            driver (webdriver.Chrome): WebDriver.
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(
            self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет данные покупателя и нажимает Continue.

        Args:
            first_name (str): Имя.
            last_name (str): Фамилия.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self) -> str:
        """
        Получает итоговую цену заказа.

        Returns:
            str: Текст с итоговой ценой (например, "$58.29").
        """
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.split()[-1]

    def finish_order(self) -> None:
        """
        Завершает оформление заказа (кнопка Finish).

        Returns:
            None
        """
        self.driver.find_element(*self.finish_button).click()

    def is_order_complete(self) -> bool:
        """
        Проверяет, что заказ успешно завершен.

        Returns:
            bool: True если заказ завершен, иначе False.
        """
        success_text = self.driver.find_element(*self.success_message).text
        return "Thank you for your order" in success_text
