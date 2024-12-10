import unittest
import time
from xml.etree.ElementPath import prepare_descendant

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.product_page import ProductPage


# Set up allure reports
@allure.feature('Flipkart')
@allure.story('Add product to cart')
class FlipkartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.flipkart.com')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @allure.title('Test Search Functionality for iPhone Product')
    def test_search_and_add_to_cart(self):
        """Test searching for an iPhone product"""
        allure.step("Search for 'iPhone' in the search bar")
        home_page = HomePage(self.driver)
        home_page.search_for_item('iphone')
        time.sleep(8)  # wait for search results to load

        allure.step("Click on APPLE brand on the left hand side filters")
        product_page = ProductPage(self.driver)
        # product_page.select_first_product()
        product_page.click_apple_brand()
        time.sleep(8)  # wait for product page to load

        allure.step("Click on 4* selection on the left hand side filters")
        product_page = ProductPage(self.driver)
        product_page.click_fourstar_rating()
        time.sleep(8)  # wait for product page to load

        allure.step("Click on ONE GB RAM selection on left hand side filters")
        product_page = ProductPage(self.driver)
        product_page.click_onegb_ram()
        time.sleep(8)  # wait for product page to load

        # allure.step("Add the product to the cart")
        # product_page.add_product_to_cart()
        # time.sleep(2)  # wait for product to be added to the cart

        # Assert that the cart contains the item
        # self.assertTrue(self.is_product_added_to_cart(), "Product not added to cart.")

        product_titles = self.driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')

        for product in product_titles:
            self.assertTrue('Apple' in product.text, f"Product '{product.text}' is not from Apple")

    # def is_product_added_to_cart(self):
    #     try:
    #         cart_button = self.driver.find_element(By.XPATH, '//span[contains(text(), "My Cart")]')
    #         cart_button.click()
    #         time.sleep(2)
    #         cart_count = self.driver.find_element(By.XPATH, '//span[@class="exehdJ"]')
    #         return int(cart_count.text) > 0
    #     except Exception as e:
    #         return False


if __name__ == '__main__':
    unittest.main()
