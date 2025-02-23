from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import json


class SmartbShoppingCartPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def shopping_cart_display(self):
        """returns the shopping cart page display"""
        return self.driver.find_element(By.CLASS_NAME, "shopping-cart-page").text

    def item_price_in_cart(self):
        """returns the item price in the shopping cart"""
        return self.driver.find_element(By.CSS_SELECTOR, ".price")

    def total_in_cart(self):
        """returns the total price in the shopping cart"""
        return self.driver.find_element(By.CLASS_NAME, "cart-summary-subtotal")

    def quantity_in_shopping_cart(self):
        """returns the quantity of item in shopping cart"""
        return self.driver.find_element(By.CSS_SELECTOR, ".qty-input").text

    def product_name_shopping_cart(self):
        """returns the product name in the shopping cart"""
        return self.driver.find_element(By.CLASS_NAME, "cart-item-link").text

    def home_page(self):
        """click on back to go to home page"""
        self.driver.back()

    def add_qty_in_shopping_cart(self):
        """Click the plus button once to increase the quantity of a product."""
        return self.driver.find_element(By.LINK_TEXT,"#/shoppingcart/updatecartitem")

    def checkout_button(self):
        """clicks on checkout button"""
        return self.driver.find_element(By.CLASS_NAME, "btn-checkout").click()











