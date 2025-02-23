import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    # Initialize the ChromeDriver service
    service=Service(executable_path="C:\Automation Tools\chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    driver.implicitly_wait(10)   # Global wait for elements
    yield driver
    driver.quit()