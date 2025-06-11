import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка выражения в калькуляторе")
@allure.description("Проверка корректности вычислений с учетом задержки")
@pytest.mark.parametrize(
    "button_sequence, expected_result, delay_value",
    [
        (["7", "+", "8", "="], "15", "4"),
        (["9", "-", "3", "="], "6", "11"),
        (["6", "*", "7", "="], "42", "30"),
        (["8", "/", "2", "="], "4", "45"),
    ],
)
def test_calculator_expressions(driver, button_sequence, expected_result, delay_value):
    page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step(f"Установка задержки: {delay_value}"):
        page.set_delay(delay_value)

    with allure.step(f"Нажатие кнопок: {' '.join(button_sequence)}"):
        for btn in button_sequence:
            page.press_button(btn)

    with allure.step("Ожидание результата"):
        start_time = time.perf_counter()
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result)
        )
        elapsed = time.perf_counter() - start_time

    with allure.step("Проверка результата на экране"):
        assert page.get_result() == expected_result

    with allure.step("Проверка времени задержки"):
        expected_time = int(delay_value)
        tolerance = 1.0
        assert (
            abs(elapsed - expected_time) <= tolerance
        ), f"Реальная задержка {elapsed:.2f} сек отличается от {expected_time} более чем на {tolerance} сек"
