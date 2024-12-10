from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    SEARCH_BAR = (By.NAME, 'q')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def search_for_item(self, item_name):
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SEARCH_BAR)
        )
        search_bar.clear()
        search_bar.send_keys(item_name)
        search_bar.send_keys(Keys.RETURN)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()
