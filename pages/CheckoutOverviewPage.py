from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utulities.Utilities import *


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def finish_item_title(self):
        finish_item_title_value = ""
        try:
            finish_item_title = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_name']")))
            finish_item_title_value = finish_item_title.text
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element finish_item_title is not found!")

        return finish_item_title_value

    def finish_item_price(self):
        finish_item_price_value = ""
        try:
            finish_item_price = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='inventory_item_price']")))
            finish_item_price_value = finish_item_price.text
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element finish_item_price is not found!")

        return finish_item_price_value

    def item_subtotal_price(self):
        item_subtotal_price_value = ""
        try:
            item_subtotal_price = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='summary_subtotal_label']")))
            item_subtotal_price_value = Utilities.leave_only_digits(item_subtotal_price.text)
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element item_subtotal_price is not found!")

        return item_subtotal_price_value

    def tax_price(self):
        tax_price_value = ""
        try:
            tax_price = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='summary_tax_label']")))
            tax_price_value = Utilities.leave_only_digits(tax_price.text)
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element tax_price is not found!")

        return tax_price_value

    def total_plus_tax_price(self):
        total_plus_tax_price_value = ""
        try:
            total_plus_tax_price = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='summary_total_label']")))
            total_plus_tax_price_value = Utilities.leave_only_digits(total_plus_tax_price.text)
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element total_plus_tax_price is not found!")

        return total_plus_tax_price_value

    def click_finish_button(self):
        try:
            finish_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn_action btn_medium cart_button']")))
            finish_button.click()
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element finish_button is not found!")

