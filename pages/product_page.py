from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    FIRST_PRODUCT = (By.XPATH, '//div[@class="_1AtVbE"]//a[@class="IRpwTa"]')
    APPLE_BRAND_SELECTION = (By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div[1]/div/label/div[1]')
    FOUR_STAR_SELECTION = (By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[5]/div[2]/div/div[1]/div/label/div[1]')
    # ONE_GB_RAM_SELECT = (By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[2]/div/label/div[1]')
    ONE_GB_RAM_SELECT = (By.XPATH,"//div[@title='1GB and Below']//div[@class='XqNaEv']")

    SIX_GB_RAM_SELECT = (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[3]/div/label/div[1]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[contains(@class,"_2KpZ6l _2U9uOA _3v1-ww")]')

    def select_first_product(self):
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )
        first_product.click()

    def click_apple_brand(self):
        apple_brand = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.APPLE_BRAND_SELECTION)
        )
        if not apple_brand.is_selected():
            apple_brand.click()

    def click_fourstar_rating(self):
        fourstar_select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FOUR_STAR_SELECTION)
        )
        if not fourstar_select.is_selected():
            fourstar_select.click()

    def click_onegb_ram(self):
        onegb_ram = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ONE_GB_RAM_SELECT)
        )
        if not onegb_ram.is_selected():
            onegb_ram.click()

    def click_sixgb_ram(self):
        sixgb_ram = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIX_GB_RAM_SELECT)
        )
        if not sixgb_ram.is_selected():
            sixgb_ram.click()

    def add_product_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart_button.click()
