import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_complete_purchase_flow():
    """
    Полный тест процесса покупки в интернет-магазине Saucedemo:
    1. Авторизация
    2. Добавление товаров в корзину
    3. Оформление заказа
    4. Проверка итоговой суммы
    """

    # 1. Настройка браузера ==============================================
    chrome_options = Options()

    # Отключаем всплывающие окна и уведомления
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")

    # Режим инкогнито для чистого теста
    chrome_options.add_argument("--incognito")

    # Дополнительные настройки для избежания проблем с автоматизацией
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

    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)

    # Устанавливаем неявное ожидание по умолчанию
    driver.implicitly_wait(5)

    # Максимизируем окно браузера
    driver.maximize_window()

    try:
        # 2. Открытие сайта ==============================================
        driver.get("https://www.saucedemo.com/")

        # Проверяем, что открылась правильная страница
        assert "Swag Labs" in driver.title, "Не удалось открыть сайт Saucedemo"

        # 3. Авторизация =================================================
        # Ждем появления поля логина (явное ожидание)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )

        # Находим остальные элементы формы
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # Вводим учетные данные стандартного пользователя
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # 4. Проверка успешной авторизации ==============================
        # Ждем появления товаров на странице
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Проверяем, что мы на странице продуктов
        assert "inventory.html" in driver.current_url, "Авторизация не удалась"

        # 5. Добавление товаров в корзину ===============================
        # Добавляем рюкзак
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Добавляем футболку
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Прокручиваем страницу вниз для видимости других товаров
        driver.execute_script("window.scrollTo(0, 500)")

        # Добавляем комбинезон
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # 6. Проверка корзины ============================================
        # Ждем обновления счетчика корзины
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        # Проверяем, что в корзине 3 товара
        assert (
                cart_badge.text == "3"
        ), f"Ожидалось 3 товара в корзине, а получили {cart_badge.text}"

        # 7. Переход к оформлению заказа =================================
        # Открываем корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Проверяем, что открылась страница корзины
        assert "cart.html" in driver.current_url, "Не удалось открыть корзину"

        # Нажимаем кнопку Checkout
        driver.find_element(By.ID, "checkout").click()

        # 8. Заполнение информации для доставки ==========================
        # Ждем появления формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        # Заполняем тестовые данные
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Продолжаем оформление
        driver.find_element(By.ID, "continue").click()

        # 9. Проверка итоговой страницы =================================
        # Проверяем, что мы на странице подтверждения
        assert (
                "checkout-step-two.html" in driver.current_url
        ), "Не удалось перейти к подтверждению заказа"

        # Проверяем наличие всех добавленных товаров
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 3, f"Ожидалось 3 товара, а получили {len(cart_items)}"

        # 10. Проверка итоговой суммы ===================================
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )

        # Извлекаем только числовое значение суммы
        total_text = total_element.text
        total_value = total_text.split()[-1]  # Получаем "$58.29"

        assert (
                total_value == "$58.29"
        ), f"Ожидалась сумма $58.29, а получили {total_value}"

        # 11. Завершение покупки =========================================
        # Для полноты теста можно добавить завершение покупки
        driver.find_element(By.ID, "finish").click()

        # Проверяем сообщение об успешном заказе
        complete_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert (
                "Thank you for your order" in complete_header.text
        ), "Заказ не был завершен успешно"

        print("\nТест успешно завершен! Все проверки пройдены.")

    except Exception as e:
        # Делаем скриншот при ошибке
        driver.save_screenshot("error_screenshot.png")
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")

    finally:
        # Закрываем браузер в любом случае
        driver.quit()


if __name__ == "__main__":
    test_complete_purchase_flow()
