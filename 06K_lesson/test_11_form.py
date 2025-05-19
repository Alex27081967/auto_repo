import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def fill_form(driver):
    """Вспомогательная функция для заполнения формы"""
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def test_zip_code_highlight(driver):
    """Тест проверяет, что поле Zip-code подсвечено красным (ошибка)"""
    fill_form(driver)
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute(
        "class"
    ), "Поле Zip-code должно быть красным"


@pytest.mark.parametrize(
    "field_id",
    [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company",
    ],
)
def test_successful_field_highlight(driver, field_id):
    """Параметризованный тест проверяет подсветку успешно заполненных полей"""
    fill_form(driver)
    field = driver.find_element(By.ID, field_id)
    assert "alert-success" in field.get_attribute(
        "class"
    ), f"Поле {field_id} должно быть зелёным"
