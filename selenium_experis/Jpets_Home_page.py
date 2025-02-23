from selenium import webdriver
from selenium.webdriver.common.by import By


class JpetsHomePage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def categories_list(self):
        """returns the list of all the categories"""
        return self.driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a")

    def category(self, category_index):
        """returns a specific category according to index"""
        return self.categories_list()[category_index]





