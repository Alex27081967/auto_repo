from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))
