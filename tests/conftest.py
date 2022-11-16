import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class") # фикстура запускается один раз для одного класса
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
    s = Service(r'C:\Users\sonya\PycharmProjects\Resources\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=chrome_options)
    request.cls.driver = driver
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    # driver.close()




