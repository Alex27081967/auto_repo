from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Открыть браузер Firefox
driver = webdriver.Firefox()

try:
    # Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Найти поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Ввести текст "Sky"
    input_field.send_keys("Sky")
    sleep(5)  # небольшая пауза для наглядности

    # Очистить поле
    input_field.clear()
    sleep(5)  # небольшая пауза для наглядности

    # Ввести текст "Pro"
    input_field.send_keys("Pro")
    sleep(5)  # небольшая пауза для наглядности

finally:
    # Закрыть браузер
    driver.quit()
