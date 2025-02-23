from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

class SmartbCartPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def remove_product_icon(self):
        """click on the remove logo"""
        self.driver.find_element(By.CLASS_NAME,"remove").click()

    def previous_page(self):
        """go to the previous page"""
        return self.driver.back()

    def unit_price(self):
        """returns the unit price of the specified product"""
        return self.driver.find_element(By.CLASS_NAME, "unit-price")

    def sub_total_price(self):
        """returns the subtotal price of the specified product"""
        return self.driver.find_element(By.CLASS_NAME, "mr-3")

    def checkout_btn(self):
        """click on the checkout button"""
        return self.driver.find_element(By.CLASS_NAME, "fa-check").click()

    def checkout(self):
        """click on the checkout button"""
        return self.driver.find_element(By.CLASS_NAME, "fa-check")

    def item_name(self):
        """returns the specified item name"""
        return self.driver.find_element(By.CSS_SELECTOR, ".name")

    def item_price(self):
        """returns the specified item price"""
        return self.driver.find_element(By.CLASS_NAME, "unit-price")

    def back_to_product_page(self):
        """click on the background next to the cart page opened from the right to go product page"""
        self.driver.find_element(By.CSS_SELECTOR, ".canvas-slidable").click()

    def product_quantity_in_cart(self):
        """returns the specified product quantity in the cart"""
        return self.driver.find_element(By.CSS_SELECTOR, "#item_EnteredQuantity")

    def product_quantity_in_cart_num(self):
        """returns the text of the specified product quantity"""
        return self.driver.find_element(By.CSS_SELECTOR, ".qty-input").text

    def product_quantity_in_cart_numbers(self):
        """returns the text of the specified product quantity"""
        return self.driver.find_element(By.CLASS_NAME, "show")

    def change_amount(self):
        """click on change amount button"""
        self.product_quantity_in_cart().click()

    def go_to_cart(self):
        """go to cart by clicking on go to cart button from cart page"""
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()

    def cart_page_display(self):
        """returns the cart display"""
        return self.driver.find_element(By.CSS_SELECTOR, ".offcanvas-cart-content")

    def cart_page_header(self):
        """returns the cart page header text as a text"""
        return self.driver.find_element(By.CSS_SELECTOR, ".offcanvas-cart-header").text

    def no_items_in_the_cart_text(self):
        """returns the cart when empty text as a text"""
        return self.driver.find_element(By.CLASS_NAME, "no-items").text















