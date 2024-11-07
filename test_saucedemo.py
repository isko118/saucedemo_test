import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Generator


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер для запуска тестов (chrome или firefox)")
    parser.addoption("--browser_version", action="store", default=None, help="Версия браузера для запуска тестов")


@pytest.fixture
def browser(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--browser"))


@pytest.fixture
def browser_version(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--browser_version"))


@pytest.fixture
def driver(browser: str, browser_version: str) -> Generator[webdriver.Chrome, None, None]:
    if browser == 'chrome':
        service = ChromeService('/opt/homebrew/bin/chromedriver')
        options = ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        service = FirefoxService('/opt/homebrew/bin/geckodriver')
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f'Unsupported browser: {browser}')
    yield driver
    driver.quit()


@allure.title("Проверка возможности входа зарегистрированного пользователя")
def test_login(driver: webdriver.Chrome) -> None:
    with allure.step("1. Открыть страницу логина"):
        driver.get('https://www.saucedemo.com/')
    with allure.step("2. Ввести в поле username логин standard_user"):
        username_input = driver.find_element(By.ID, 'user-name')
        username_input.send_keys('standard_user')
    with allure.step("3. Ввести в поле password пароль secret_sauce"):
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys('secret_sauce')
    with allure.step("4. Нажать кнопку Login"):
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    with allure.step("5. Проверить, что открыта страница с товарами"):
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        inventory_list = driver.find_element(By.CLASS_NAME, 'inventory_list')
        assert inventory_list is not None


@allure.title("Проверка возможности выхода залогиненного пользователя")
def test_logout(driver: webdriver.Chrome) -> None:
    with allure.step("1. Войти на сайт"):
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
    with allure.step("2. Открыть меню пользователя"):
        menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
        menu_button.click()
    with allure.step("3. Нажать на кнопку Logout"):
        wait = WebDriverWait(driver, 10)
        logout_link = wait.until(EC.visibility_of_element_located((By.ID, 'logout_sidebar_link')))
        logout_link.click()
    with allure.step("4. Проверить, что пользователь вышел из аккаунта"):
        assert driver.current_url == 'https://www.saucedemo.com/'
