import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    # Настройки Chrome
    options = Options()
    driver = webdriver.Chrome(options=options)

    try:
        # 1. Открыть страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        # 2. Установить задержку 45 секунд
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажать кнопки 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Дождаться результата (45 секунд максимум + запас)
        output_locator = (By.CLASS_NAME, "screen")
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(output_locator, "15")
        )

        # 5. Проверка
        result = driver.find_element(*output_locator).text
        assert result == "15", f"Ожидался результат 15, но получено: {result}"

    finally:
        driver.quit()
