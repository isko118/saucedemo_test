
# Тестирование сайта Saucedemo

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0.0-green.svg)
![pytest](https://img.shields.io/badge/pytest-7.0.0-orange.svg)
![Allure](https://img.shields.io/badge/Allure-2.20.1-purple.svg)
![mypy](https://img.shields.io/badge/mypy-0.910-blue.svg)
![ruff](https://img.shields.io/badge/ruff-0.0.278-red.svg)

## Описание

Этот проект содержит автоматические тесты для проверки аутентификации, авторизации и выхода пользователя на сайте [Saucedemo](https://www.saucedemo.com/). Тесты написаны на Python с использованием библиотек Selenium и pytest, а также поддерживают генерацию отчетов Allure.

## Требования

- **Python** 3.11+
- **Chrome** или **Firefox** браузер
- **Chromedriver** или **Geckodriver**, соответствующий версии вашего браузера
- Установленный **Allure Commandline** для генерации отчетов
- **Java** 8 или выше (для Allure)

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/yourusername/saucedemo-tests.git
   ```

2. **Перейдите в директорию проекта:**

   ```bash
   cd saucedemo-tests
   ```

3. **Создайте и активируйте виртуальное окружение:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Обновите pip:**

   ```bash
   pip install --upgrade pip
   ```

5. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Установите драйвер браузера:**

   - **Chrome:**
     - Скачайте [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), соответствующий версии вашего браузера.
     - Поместите `chromedriver` в `/usr/local/bin/` или укажите путь в коде.
   - **Firefox:**
     - Скачайте [Geckodriver](https://github.com/mozilla/geckodriver/releases).
     - Поместите `geckodriver` в `/usr/local/bin/` или укажите путь в коде.

7. **Установите Allure Commandline:**

   - **macOS (через Homebrew):**

     ```bash
     brew install allure
     ```

## 🧪 Запуск тестов

### Запуск всех тестов в браузере Chrome:

```bash
pytest --browser=chrome
```

### Запуск тестов в браузере Firefox:

```bash
pytest --browser=firefox
```

### Выбор версии браузера (при необходимости):

```bash
pytest --browser=chrome --browser_version=91.0
```

## Генерация Allure отчета

1. **Сбор результатов тестов:**

   ```bash
   pytest --alluredir=allure-results
   ```

2. **Просмотр отчета:**

   ```bash
   allure serve allure-results
   ```

   Эта команда сгенерирует отчет и автоматически откроет его в браузере.

