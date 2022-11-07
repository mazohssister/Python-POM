from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InventoryPage import InventoryPage


class InventoryItemPage(InventoryPage):

    def __init__(self, driver):
        self.driver = driver

    def item_title_iip(self):

        try:
            item_title_iip = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_details_name large_size']")))
            item_title_value_iip = item_title_iip.text
            return item_title_value_iip
        except TimeoutException:
            self.driver.implicitly_wait(10)
            print("Element item_title_iip is not found!")

    def item_price_iip(self):

        try:
            item_title_iip = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_details_price']")))
            item_title_value_iip = item_title_iip.text
            return item_title_value_iip
        except TimeoutException:
            self.driver.implicitly_wait(10)
            print("Element item_price_iip is not found!")

    def add_to_cart(self):
        """Add item to cart without open it"""
        try:
            add_to_cart_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")))
            add_to_cart_button.click()

        except TimeoutException:
            self.driver.implicitly_wait(10)
            print("Element add_to_cart_button is not found!")

        """Open a shopping cart"""
        try:
            shopping_cart_button = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
            shopping_cart_button.click()

        except TimeoutException:
            self.driver.implicitly_wait(10)
            print("Element open a cart is not found!")


