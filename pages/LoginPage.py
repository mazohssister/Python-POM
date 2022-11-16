from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, test_login_value, test_password_value):

        self.driver.implicitly_wait(10)
        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name.send_keys(test_login_value)

        password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        password.send_keys(test_password_value)
        password.submit()
