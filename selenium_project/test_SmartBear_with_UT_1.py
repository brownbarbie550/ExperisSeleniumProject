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
from selenium.webdriver.support.ui import WebDriverWait
import json


class TestSmartBearWithUT(TestCase):
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

    """question1"""
    def test_transferring_to_certain_category_page(self):
        """checks the transferring to the chosen category page and
        verifies that the category name matches to the one from home page"""
        self.home_page.choose_category()
        self.assertEqual(self.home_page.category_name(), self.product_page.product_name())

    def test_the_matching_of_product_names(self):
        """add product to the cart and
        verify the name of the product matches to the selected one"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.assertEqual(self.category_page.product_name().text, self.product_page.product_name())

    def test_return_to_category_page(self):
        """go to category page and verify it's done"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.previous_page()
        self.assertTrue(self.category_page.category_page_display())

    def test_return_to_home_page(self):
        """go to home page and verify it's done"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.previous_page()
        self.category_page.previous_page()
        self.assertIn("Welcome to our store.", self.home_page.home_page_display())

    """question2"""
    def test_add_2_of_product_to_the_cart(self):
        """add 2 of product to the cart different amount each
        and verify that the total amount in the cart is correct"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity2()
        self.product_page.add_to_cart()
        """"returns= to home page and add the second product"""
        self.home_page.home_page_icon()
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity3()
        self.product_page.add_to_cart()
        sleep(3)
        self.assertIn("5", self.cart_page.product_quantity_in_cart_numbers().text)


    """question3"""
    def test_add_3_products(self):
        """add 3 products with different amount each
        and verify that the product name, product price and product quantity
        matches in both product page and the cart"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity2()
        self.product_page.add_to_cart()
        """back to home page in order to choose another category and product"""
        self.cart_page.previous_page()
        sleep(2)
        self.home_page.home_page_icon()
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity3()
        self.product_page.add_to_cart()
        """back to home page in order to choose another category and product"""
        self.cart_page.previous_page()
        sleep(2)
        self.home_page.home_page_icon()
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity4()
        self.product_page.add_to_cart()
        sleep(3)
        self.assertEqual(self.product_page.quantity().text, self.cart_page.product_quantity_in_cart().text)
        self.assertEqual(self.product_page.product_name(), self.cart_page.item_name().text)
        self.assertEqual(self.product_page.product_price().text, self.cart_page.item_price().text)
        sleep(3)

    """question4"""
    def test_add_2_products(self):
        """add 2 products to the cart remove 1 of them
        and verify that the quantity is updated accordingly"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        self.cart_page.previous_page()
        """back to home page and choose another product"""
        self.home_page.home_page_icon()
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        sleep(2)
        self.cart_page.remove_product_icon()
        sleep(5)
        self.assertIn("1", self.cart_page.product_quantity_in_cart_numbers().text)

    """question5a"""
    def test_add_product_and_cart_open(self):
        """add product to the cart and verify that cart page opens from the right side of the screen"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        sleep(3)
        self.assertIn("Shopping Cart", self.cart_page.cart_page_header())

    """question5b"""
    def test_click_on_background(self):
        """after the cart page opens as a result of adding product to the cart
        click on the background and verify the cart page closes"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        self.cart_page.back_to_product_page()
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.product_page.product_page_display())
        self.assertIn("Add to List", self.product_page.product_page_details_text())

    """question5c"""
    def test_shopping_basket(self):
        """click on the shopping basket logo and verify that the shopping basket opens"""
        self.home_page.shopping_basket_logo()
        sleep(5)
        self.assertIn("Shopping Cart", self.cart_page.cart_page_header())

    """question5d"""
    def test_go_to_cart_btn(self):
        """click on go to cart button and verify that shopping cart page opens"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        self.cart_page.go_to_cart()
        sleep(2)
        self.assertIn("I have a discount code", self.shopping_cart_page.shopping_cart_display())

    """question6"""
    def test_product_in_cart_details(self):
        """add 3 product with different amount each to the cart and verify that the subtotal price
        and the quantity matches both in the cart page and the shopping cart page"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity2()
        self.product_page.add_to_cart()
        print(f"the selected product name is: {self.cart_page.item_name().text}")
        print(f"the selected product quantity is: {self.cart_page.product_quantity_in_cart_num()}")
        print(f"the selected product price is: {self.cart_page.sub_total_price().text}")
        sleep(2)
        self.cart_page.go_to_cart()
        print(self.shopping_cart_page.total_in_cart().text)
        sleep(5)

        """back to home page in order to choose another category and product"""
        self.home_page.home_page_icon()
        sleep(2)
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity3()
        self.product_page.add_to_cart()
        print(f"the selected product name is: {self.cart_page.item_name().text}")
        print(f"the selected product quantity is: {self.cart_page.product_quantity_in_cart_num()}")
        print(f"the selected product price is: {self.cart_page.sub_total_price().text}")
        self.cart_page.go_to_cart()
        print(self.shopping_cart_page.total_in_cart().text)
        sleep(5)

        """back to home page in order to choose another category and product"""
        self.home_page.home_page_icon()
        sleep(2)
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.clear_quantity()
        self.product_page.add_quantity4()
        self.product_page.add_to_cart()
        print(f"the selected product name is: {self.cart_page.item_name().text}")
        print(f"the selected product quantity is: {self.cart_page.product_quantity_in_cart_num()}")
        print(f"the selected product price is: {self.cart_page.sub_total_price().text}")
        self.cart_page.go_to_cart()
        print(self.shopping_cart_page.total_in_cart().text)
        sleep(5)
        self.assertIn(self.cart_page.sub_total_price().text, self.shopping_cart_page.shopping_cart_display())
        self.assertIn(self.cart_page.product_quantity_in_cart_num(), self.shopping_cart_page.shopping_cart_display())



    """question7abc"""
    def test_add_2_products_and_change_quantity(self):
        """add 2 products to the cart and change the both products quantity
        in the shopping cart page and verify it's updated"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        self.cart_page.previous_page()
        self.home_page.home_page_icon()
        """choose and add another product with different quantity to the cart"""
        self.home_page.choose_category()
        self.category_page.choose_product()
        self.product_page.add_to_cart()
        self.cart_page.go_to_cart()
        sleep(3)
        price_before_update = self.shopping_cart_page.item_price_in_cart().text
        total_before_update = self.shopping_cart_page.total_in_cart().text
        print(f"price before is: {price_before_update}")
        print(f"total before is: {total_before_update}")
        self.shopping_cart_page.add_qty_in_shopping_cart().clear()
        self.shopping_cart_page.add_qty_in_shopping_cart().send_keys("4")
        price_after_update = self.shopping_cart_page.item_price_in_cart().text
        total_after_update = self.shopping_cart_page.total_in_cart().text
        print(f"price before is: {price_after_update}")
        print(f"total before is: {total_after_update}")
        print(json.dumps({"price_before": price_before_update, "total_before": total_before_update}))

        self.assertNotEqual(total_before_update, total_after_update)
        self.assertNotEqual(price_after_update, price_before_update)

        self.home_page.home_page_icon()
        self.home_page.shopping_basket_logo()
        self.assertEqual(self.shopping_cart_page.total_in_cart().text, self.cart_page.sub_total_price().text)
    """"only part of the test works """


    """question8"""
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




























