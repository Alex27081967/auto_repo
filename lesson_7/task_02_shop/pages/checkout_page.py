from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.split()[-1]  # Получаем "$58.29"

    def finish_order(self):
        self.driver.find_element(*self.finish_button).click()

    def is_order_complete(self):
        return (
                "Thank you for your order"
                in self.driver.find_element(*self.success_message).text
        )
