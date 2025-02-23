from unittest import TestCase
from selenium import webdriver
from time import sleep
from Smartb_Home_Page import SmartbHomePage
from Smartb_Category_Page import SmartbCategoryPage
from Smartb_Product_Page import SmartbProductPage
from Smartb_Cart_Page import SmartbCartPage
from Smartb_Shopping_Cart_Page import SmartbShoppingCartPage
from Smartb_Login_Page import SmartbLoginPage
from Smartb_Checkout_Page import SmartbCheckoutPage
import re


class TestSmartBearWithUT8(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home_page = SmartbHomePage(self.driver)
        self.category_page = SmartbCategoryPage(self.driver)
        self.product_page = SmartbProductPage(self.driver)
        self.cart_page = SmartbCartPage(self.driver)
        self.shopping_cart_page = SmartbShoppingCartPage(self.driver)
        self.login_page = SmartbLoginPage(self.driver)
        self.checkout_page = SmartbCheckoutPage(self.driver)


    def test_order_approval(self):
        """add 2 products to the cart click on checkout and after login to existing user
        verify that the order approval text appears"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        self.cart_page.go_to_cart()
        sleep(3)
        self.shopping_cart_page.checkout_button()
        sleep(2)
        self.login_page.username_or_email_filed().send_keys("BrownBarbie")
        self.login_page.password_field().send_keys("smartbear321")
        self.login_page.login_button()
        sleep(5)
        self.shopping_cart_page.checkout_button()
        sleep(3)
        self.checkout_page.billing_address_button()
        self.checkout_page.shipping_address_button()
        self.checkout_page.next_button_after_address_approving()
        self.checkout_page.next_button_before_payment_page()
        self.checkout_page.terms_of_service_and_privacy_terms()
        self.checkout_page.confirm_button()
        sleep(2)
        self.checkout_page.order_details_button()
        sleep(2)
        self.home_page.shopping_basket_logo()
        sleep(3)
        print(self.cart_page.no_items_in_the_cart_text())

        """strips the text that the methods returns using re which finds the first sequence of digits in the string 
        in order to do the test only on the numbers"""
        checkout_order_number = re.search(r'\d+', self.checkout_page.order_number_in_checkout_page()).group()
        order_page_order_number = re.search(r'\d+', self.checkout_page.order_number_in_order_page()).group()
        self.assertEqual(checkout_order_number, order_page_order_number)

        """"checks the cart is empty by verifying the shopping cart empty text appears"""
        self.assertIn("Shopping cart empty" ,self.cart_page.no_items_in_the_cart_text())


    """"question9"""
    def test_login(self):
        """complete a login process and verify that it's works"""
        self.home_page.user_login_icon()
        sleep(2)
        self.login_page.username_or_email_filed().send_keys("BrownBarbie")
        self.login_page.password_field().send_keys("smartbear321")
        self.login_page.login_button()
        self.assertIn("BROWNBARBIE", self.home_page.user_account_logo())



    def test_logout(self):
        """complete a logout process and verify that it's works"""
        self.home_page.user_login_icon()
        self.login_page.username_or_email_filed().send_keys("BrownBarbie")
        self.login_page.password_field().send_keys("smartbear321")
        self.login_page.login_button()
        self.home_page.user_account_dropdown_list()
        self.home_page.user_logout_button()
        self.assertIn("LOG IN", self.home_page.user_login_text())











