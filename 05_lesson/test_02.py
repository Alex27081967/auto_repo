from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Правильная инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com")
print(driver.title)
driver.quit()
