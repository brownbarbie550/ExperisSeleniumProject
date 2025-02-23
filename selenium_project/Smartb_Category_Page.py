from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

class SmartbCategoryPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def random_product(self):
        """returns a random product"""
        return self.driver.find_element(By.CSS_SELECTOR, ".art-name>a")

    def choose_product(self):
        """click on the random product"""
        self.random_product().click()

    def back_to_home_page(self):
        """return to home page by clicking on the brand logo"""
        self.driver.find_element(By.CSS_SELECTOR, ".brand")

    def product_name(self):
        """returns the product name"""
        return self.driver.find_element(By.CLASS_NAME, "page-title")

    def item_name(self):
        """returns the text out of the product name"""
        self.product_name().get_attribute("title")

    def previous_page(self):
        """go to the previous page"""
        return self.driver.back()

    def category_name(self):
        """returns the category name"""
        return self.driver.find_element(By.CSS_SELECTOR, ".h3").text

    def category_page_display(self):
        """returns category page display"""
        return self.driver.find_element(By.CLASS_NAME, "page-main")





