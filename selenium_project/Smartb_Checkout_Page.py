from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

class SmartbCheckoutPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def firstname_filed(self):
        """returns firstname filed"""
        return self.driver.find_element(By.ID, "#NewAddress_FirstName")

    def lastname_filed(self):
        """returns lastname filed"""
        return self.driver.find_element(By.ID, "#NewAddress_LastName")

    def next_button(self):
        """clicks on the next button"""
        self.driver.find_element(By.CLASS_NAME, "new-address-next-step-button").click()

    def billing_address_button(self):
        """clicks on the billing address button"""
        self.driver.find_element(By.CLASS_NAME, "select-billing-address-button").click()

    def shipping_address_button(self):
        """clicks on the shipping address button"""
        self.driver.find_element(By.CLASS_NAME, "select-shipping-address-button").click()

    def next_button_after_address_approving(self):
        """clicks on the next button after address approving"""
        self.driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button").click()

    def next_button_before_payment_page(self):
        """clicks on the next button before payment page"""
        self.driver.find_element(By.CLASS_NAME, "payment-method-next-step-button").click()

    def next_button_payment(self):
        """clicks on the next button in payment page"""
        self.driver.find_element(By.CLASS_NAME, "payment-method-next-step-button").click()

    def confirm_button(self):
        """clicks on confirm button"""
        self.driver.find_element(By.CLASS_NAME, "btn-buy").click()

    def terms_of_service_and_privacy_terms(self):
        """clicks on the check button of terms of service and privacy terms"""
        self.driver.find_element(By.CLASS_NAME, "form-check-input").click()

    def order_number_in_checkout_page(self):
        """returns the order number from the checkout page after confirming the order and it's details"""
        return self.driver.find_element(By.CLASS_NAME, "page-body").text

    def continue_shopping_button(self):
        """clicks on continue shopping button after confirming the order and it's details"""
        self.driver.find_element(By.CLASS_NAME, "order-completed-continue-button").click()

    def order_details_button(self):
        """clicks on order details button after confirming the order and it's details"""
        """clicks on order details button after con"""
        self.driver.find_element(By.CLASS_NAME, "btn-warning").click()

    def order_number_in_order_page(self):
        """returns the order number from order page"""
        return self.driver.find_element(By.CLASS_NAME, "col-sm-auto").text