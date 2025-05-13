from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Открыть браузер Google Chrome
driver = webdriver.Chrome()

try:
    # 2. Перейти на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # 3. Найти кнопку по XPath (по тексту на кнопке)
    button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"
    )

    # 4. Кликнуть на синюю кнопку
    button.click()
    print("Кнопка успешно нажата!")

    # Пауза для визуальной проверки
    sleep(5)

finally:
    # Закрыть браузер
    driver.quit()
