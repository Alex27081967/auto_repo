from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор страницы калькулятора.

        :param driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.button_map = {"/": "÷", "*": "x"}

    def open(self) -> None:
        """
        Открывает веб-страницу калькулятора.
        """
        self.driver.get(self.url)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку.

        :param value: Задержка в секундах (строка или число)
        """
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(value))

    def press_button(self, label: str) -> None:
        """
        Нажимает кнопку на калькуляторе.

        :param label: Текст кнопки (например, '7', '+', '=')
        """
        display_label = self.button_map.get(label, label)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{display_label}']"))
        )
        button.click()

    def get_result(self) -> str:
        """
        Получает результат с экрана.

        :return: Строка с результатом (например, '42')
        """
        screen = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        )
        return screen.text
