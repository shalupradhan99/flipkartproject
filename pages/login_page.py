from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    LOGIN_BUTTON = (By.XPATH, '//a[@href="/account/login"]')
    MOBILE_NUMBER_INPUT = (By.XPATH, '//input[@class="_2IX_2- VJZDxU"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ERROR_MESSAGE = (By.XPATH, '//span[contains(text(),"Enter valid")]')  # Error message for invalid login

    def open_login_page(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()

    def login(self, mobile_number, password):
        mobile_number_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MOBILE_NUMBER_INPUT)
        )
        mobile_number_input.send_keys(mobile_number)

        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()

    def get_error_message(self):
        try:
            error_message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error_message.text
        except:
            return None
