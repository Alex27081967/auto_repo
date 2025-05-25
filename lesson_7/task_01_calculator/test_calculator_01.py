import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# Параметризация: выражения, результат, задержка
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
    page.open()

    # Установка задержки
    page.set_delay(delay_value)

    # Вводим выражение по шагам
    for btn in button_sequence:
        page.press_button(btn)

    # Засекаем время начала ожидания
    start_time = time.perf_counter()

    # Ждём результат
    wait = WebDriverWait(driver, 46)
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result)
    )

    # Засекаем время окончания
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    # Эталон времени
    expected_time = int(delay_value)
    tolerance = 1.0  # допустимое отклонение

    # Лог
    print(f"\n[INFO] Выражение: {' '.join(button_sequence)}")
    print(f"[INFO] Указанная задержка: {delay_value} сек")
    print(f"[INFO] Реальное ожидание: {elapsed:.2f} сек")

    # Проверки
    assert page.get_result() == expected_result, f"Ожидался результат {expected_result}"
    assert (
        abs(elapsed - expected_time) <= tolerance
    ), f"Реальная задержка {elapsed:.2f} сек отличается от {expected_time} более чем на {tolerance} сек"
