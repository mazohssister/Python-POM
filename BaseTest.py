from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class BaseTest:  # pattern single tone

    def __init__(self, base_url='https://www.saucedemo.com/'):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        s = Service(r'C:\Users\sonya\PycharmProjects\Resources\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.get(base_url)
