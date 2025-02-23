from selenium import webdriver
from selenium.webdriver.common.by import By


class PetsCartPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver


    def table_rows(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr")[1:-1]

    def quantity(self, row_index):
        return self.table_rows()[row_index].find_element(By.CSS_SELECTOR, "td>input")

    def type_quantity(self,row_index, qty_value):
        self.quantity(row_index).clear()
        self.quantity(row_index).send_keys(qty_value)

    def list_price(self, row_index):
        return self.table_rows()[row_index].find_elements(By.TAG_NAME, "td")[5]

    def list_price_text(self, row_index):
        return self.list_price(row_index).text

    def update_quantity(self):
        return self.driver.find_element(By.NAME, "updateCartQuantities").click()


