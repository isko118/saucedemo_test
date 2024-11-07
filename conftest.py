import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--browser", action="store", default="chrome", help="Браузер для запуска тестов (chrome или "
                                                                         "firefox)")
    parser.addoption("--browser_version", action="store", default=None, help="Версия браузера для запуска тестов")
