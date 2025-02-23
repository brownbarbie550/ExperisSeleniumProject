from selenium import webdriver
from selenium.webdriver.common.by import By


class PetsItemsPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def table_rows(self):
        """return all the items rows (excluding the header and the last row)"""
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")[1:-1]

    def item_add_to_cart(self, row_index):
        return self.table_rows()[row_index].find_element(By.CLASS_NAME, "Button")

    def click_add_to_cart(self, row_index):
        self.item_add_to_cart(row_index).click()


