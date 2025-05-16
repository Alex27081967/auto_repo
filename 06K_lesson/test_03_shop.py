from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument(
        "--incognito"
    )  # Режим инкогнито, чтобы обойти сохранённые данные
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"]
    )
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")

    try:
        # Авторизация
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Ожидание загрузки страницы с товарами
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Добавление товаров в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.execute_script("window.scrollTo(0, 500)")  # Прокрутка вниз
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Проверка количества товаров в корзине
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == "3", "Ожидалось 3 товара в корзине"

    finally:
        driver.quit()
