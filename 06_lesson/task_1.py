from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Создаем экземпляр веб-драйвера (например, для Chrome)
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Находим кнопку и нажимаем на неё
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    # Ждем, пока текст появится на странице
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content .bg-success"))
    )

    # Получаем текст из зеленой плашки
    success_text = driver.find_element(By.CSS_SELECTOR, "#content .bg-success").text

    # Выводим текст в консоль
    print(success_text)

finally:
    # Закрываем браузер
    driver.quit()
