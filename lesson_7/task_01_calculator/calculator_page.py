from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса. Принимает webdriver (Chrome, Firefox и т.д.).
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Сопоставление логических символов операций с отображаемыми на кнопках
        self.button_map = {"/": "÷", "*": "x"}  # Деление  # Умножение

    def open(self):
        """
        Открывает веб-страницу калькулятора.
        """
        self.driver.get(self.url)

    def set_delay(self, value):
        """
        Устанавливает значение задержки (в секундах) в поле #delay.
        :param value: Строка или число, которое будет введено в поле задержки.
        """
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(value))

    def press_button(self, label):
        """
        Нажимает кнопку калькулятора.
        Автоматически заменяет логические символы (/, *) на отображаемые на сайте (÷, x).
        :param label: Текст кнопки (например, '7', '+', '=' или '*')
        """
        # Если кнопка в маппинге, используем замену
        display_label = self.button_map.get(label, label)

        # Ожидаем появления кнопки на странице и кликаем
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{display_label}']"))
        )
        button.click()

    def get_result(self):
        """
        Получает текущий текст на дисплее калькулятора (class="screen").
        :return: Строка с результатом (например, '15')
        """
        screen = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        )
        return screen.text
