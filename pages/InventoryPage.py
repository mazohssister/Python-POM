from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def find_and_click_item(self, product_number):
        """Find & add to the cart from the item"""

        try:
            item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='inventory_item_name'])[" + product_number + "]")))
            item.click()
        except TimeoutException:
            self.driver.implicitly_wait(10)
            print("Element find_and_click_item is not found!")


    def item_title_ip(self, product_number):
        item_title_value_ip = ""

        try:
            item_title = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='inventory_item_name'])["+product_number+"]")))
            item_title_value_ip = item_title.text
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element item_title_ip is not found!")

        return item_title_value_ip

    def item_price_ip(self, product_number):
        item_price_value_ip = ""

        try:
            item_price = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='inventory_item_price'])["+product_number+"]")))
            item_price_value_ip = item_price.text
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element item_price_ip is not found!")
        return item_price_value_ip

