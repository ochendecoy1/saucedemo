import pytest
from selenium import webdriver

# контекстный менеджер, надо
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()