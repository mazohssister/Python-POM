from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    first_name_value = "Sofiia"
    last_name_value = "Litvinova"
    zip_code_value = "188666"

    def __init__(self, driver):
        self.driver = driver

    def checkout_cart_find_click(self):
        try:
            checkout_cart_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")))
            checkout_cart_button.click()
        except TimeoutException:
            self.driver.implicitly_wait(5)
            print("Element checkout_cart_find_click is not found!")

    def fill_checkout_form(self):

        """Fill checkout form & click continue"""

        first_name = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        first_name.send_keys(self.first_name_value)

        last_name = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        last_name.send_keys(self.last_name_value)

        zip_code = self.driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']")
        zip_code.send_keys(self.zip_code_value)

        continue_button = self.driver.find_element(By.XPATH,
                                                   "//input[@class='submit-button btn btn_primary cart_button btn_action']")
        continue_button.click()
