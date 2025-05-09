from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание появления текста "Done!" — сигнал, что всё загрузилось
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    # Получаем все <img> с непустым src
    images_with_src = [
        img
        for img in driver.find_elements(By.TAG_NAME, "img")
        if img.get_attribute("src")
    ]

    # Вывод количества изображений с src
    print(f"Количество изображений с src: {len(images_with_src)}")

    # Вывод src третьей картинки, если есть
    if len(images_with_src) >= 3:
        print("SRC третьей картинки:", images_with_src[2].get_attribute("src"))
    else:
        print("Третья картинка с src не найдена")

finally:
    driver.quit()
