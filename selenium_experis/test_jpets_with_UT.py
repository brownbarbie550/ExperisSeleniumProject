from unittest import TestCase
from selenium import webdriver
from Jpets_Home_page import JpetsHomePage
from Jpets_Product_Page import JpetsProductPage
from time import sleep
from Pets_Items_Page import PetsItemsPage
from Pets_Cart_page import PetsCartPage
from random import randint
from random import choice

from selenium_experis.jpetstore_test import list_price_value


class TestJpetsWithUT(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # Go to the required URL
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        # Maximize the window
        self.driver.maximize_window()
        # Define a timeout: In case an element is not found - wait 10 seconds
        self.driver.implicitly_wait(10)
        self.home_page = JpetsHomePage(self.driver)
        self.product_page = JpetsProductPage(self.driver)
        self.items_page = PetsItemsPage(self.driver)
        self.cart_page = PetsCartPage(self.driver)

    def test_add_item_to_cart(self):
        choice(self.home_page.categories_list()).click() #click random category
        product_rows = self.product_page.table_data_rows()
        random_index = randint(0, len(product_rows)-1) #choose random index
        print(f"we chose {self.product_page.product_name_text(random_index)}")
        self.product_page.product_id_click(random_index)

        items_rows = self.items_page.table_rows()
        random_index = randint(0, len(items_rows)-1) #choose random index of item
        self.items_page.click_add_to_cart(random_index)

        self.cart_page.type_quantity(-1, "7") #update quantity of the last row
        self.cart_page.update_quantity()


    def test_cart_total_calculation(self):
        driver = self.driver

        list_price = driver.find_element(By.ID, "price")
        fish_quantity = driver.find_element(By.NAME, "EST-20")
        total_price = driver.find_element(By.ID, "total")

        list_price_value = float(list_price.text.strip().replace("$", "").replace(",", ""))
        fish_quantity_value = int(fish_quantity.get_attribute("value").strip())
        total_price_value = float(total_price.text.strip().replace("$", "").replace(",", ""))

    def tearDown(self):
        sleep(4)
        self.driver.quit()