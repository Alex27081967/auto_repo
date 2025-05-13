from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Настройка Firefox
options = Options()

driver = webdriver.Firefox(options=options)

try:
    # Переходим на страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поле username и вводим значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Находим поле password и вводим значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Находим кнопку Login и кликаем
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Ждем появления сообщения (можно добавить явное ожидание)
    sleep(5)

    # Находим элемент с сообщением и выводим текст в консоль
    message = driver.find_element(By.ID, "flash")
    print("Сообщение после авторизации:", message.text.strip())

    # Пауза для визуальной проверки (можно убрать)
    sleep(5)

finally:
    # Закрываем браузер
    driver.quit()
