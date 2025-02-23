from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

class SmartbLoginPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def username_or_email_filed(self):
        """returns the username or email filed"""
        return self.driver.find_element(By.CLASS_NAME, "username")

    def password_field(self):
        """returns the password field"""
        return self.driver.find_element(By.CLASS_NAME, "password")

    def login_button(self):
        """clicks on the login button"""
        return self.driver.find_element(By.CLASS_NAME, "btn-login").click()

