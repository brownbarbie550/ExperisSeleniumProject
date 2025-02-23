from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

class SmartbHomePage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def category_icons(self):
        """returns the categories"""
        return self.driver.find_elements(By.XPATH, "//*[@id='content-center']/div/div/div[2]/article")

    def random_category(self):
        """returns a random category"""
        return self.driver.find_element(By.CLASS_NAME, "art-genericname")

    def choose_category(self):
        """click on the randomly chosen category"""
        # self.random_category().click()
        choose_category = self.driver.find_elements(By.XPATH, "//*[@id='content-center']/div/div/div[2]/article")
        random_index = randint(0, len(choose_category) - 1)
        random_category = choose_category[random_index]
        random_category.click()

    def previous_page(self):
        """go to the previous page"""
        return self.driver.back()

    def category_name(self):
        """returns category name from home page"""
        return self.driver.find_element(By.CSS_SELECTOR, ".art-genericname").text

    def home_page_display(self):
        """returns home page display"""
        return self.driver.find_element(By.CLASS_NAME, "page-main").text

    def welcome_text_home_page(self):
        """returns the welcome text from home page as a text"""
        return self.driver.find_element(By.CLASS_NAME, "h2").text

    def home_page_icon(self):
        """clicks on home page icon"""
        self.driver.find_element(By.CLASS_NAME, "brand").click()

    def shopping_basket_logo(self):
        """clicks on shopping basket icon"""
        self.driver.find_element(By.CLASS_NAME, "icm-bag").click()

    def user_login_icon(self):
        """clicks on user login icon"""
        self.driver.find_element(By.CLASS_NAME, "fa-user-circle").click()

    def user_login_text(self):
        """returns user login text as a text"""
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/header/div[1]/div/nav/nav[4]/div/a").text

    def user_account_logo(self):
        """returns the text from the user account logo"""
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/header/div[1]/div/nav/nav[4]/div").text

    def user_account_dropdown_list(self):
        """clicks on the user account dropdown list"""
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/header/div[1]/div/nav/nav[4]/div/a/i[2]").click()

    def user_logout_button(self):
        """clicks on the user logout button"""
        self.driver.find_element(By.CLASS_NAME, "fa-sign-out-alt").click()