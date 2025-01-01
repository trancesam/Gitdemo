import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "edge":
        driver = webdriver.Edge()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    request.cls.driver=driver
    yield
    driver.close()