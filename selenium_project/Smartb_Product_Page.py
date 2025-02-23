from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

class SmartbProductPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def quantity(self):
        """returns the quantity field in the product page"""
        return self.driver.find_element(By.CSS_SELECTOR, ".form-control-lg")

    def clear_quantity(self):
        """clears the quantity field"""
        self.quantity().clear()

    def add_quantity2(self):
        """enters the required amount in the quantity filed"""
        self.quantity().send_keys("2")

    def add_quantity3(self):
        """enters the required amount in the quantity filed"""
        self.quantity().send_keys("3")

    def add_quantity4(self):
        """enters the required amount in the quantity filed"""
        self.quantity().send_keys("4")

    def add_to_cart(self):
        """click on the add to cart button"""
        self.driver.find_element(By.CSS_SELECTOR, ".btn-add-to-cart").click()

    def previous_page(self):
        """go to category page"""
        return self.driver.back()

    def product_price(self):
        """returns the specified product price"""
        return self.driver.find_element(By.CLASS_NAME, "pd-price")

    def product_name(self):
        """returns the specified product name"""
        return self.driver.find_element(By.CLASS_NAME, "page-title").text

    def product_quantity(self):
        """returns the specified product quantity entered"""
        return self.driver.find_element(By.CLASS_NAME, "fa-cart-arrow-down")

    def shopping_cart(self):
        """click on the shopping cart logo"""
        self.driver.find_element(By.CLASS_NAME, "icm-bag").click()

    def product_page_display(self):
        """returns the product page display"""
        return self.driver.find_element(By.CSS_SELECTOR, "#content-wrapper")

    def product_page_details(self):
        """returns the product details in the product page"""
        self.driver.find_element(By.CSS_SELECTOR, ".pd-offer")

    def product_page_details_text(self):
        """returns the product details in the product page"""
        return self.driver.find_element(By.CSS_SELECTOR, ".pd-offer").text







