import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    # Создаем объект сервиса с указанием пути к драйверу
    service = Service("C:/ProgramData/chocolatey/bin/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Устанавливаем тайм-аут ожидания
    yield driver
    driver.quit()  # Закрытие браузера после завершения теста
