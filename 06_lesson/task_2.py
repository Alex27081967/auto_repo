from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

try:
    # Переходим на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода по его ID и вводим текст "SkyPro"
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # Находим синюю кнопку и нажимаем на нее
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    # Получаем текст кнопки и выводим его в консоль
    button_text = button.text
    print("Текст кнопки:", button_text)  # Ожидается, что текст будет "SkyPro"

finally:
    # Закрываем драйвер
    driver.quit()
