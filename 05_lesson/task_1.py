from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Google Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Ждем загрузки страницы
    sleep(5)

    # Находим синюю кнопку по CSS-классу и кликаем на нее
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    # Ждем немного перед закрытием браузера
    sleep(5)


finally:
    # Закрываем браузер
    driver.quit()
