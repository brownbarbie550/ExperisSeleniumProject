from selenium import webdriver
from Calc_Page import CalcPage
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://juliemr.github.io/protractor-demo/")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

calc_page = CalcPage(driver)  #create calc page object

#calculate 5 * 9
calc_page.type_number1("5")
calc_page.choose_operator("*")
calc_page.type_number2("9")
calc_page.click_go()

#check the result
if calc_page.final_result_text() == "45":
    print("test passed")
else:
    print(f"test failed, result is {calc_page.final_result_text()}")

#check that both numbers fields are empty
if calc_page.number1_value() == "":
    print("test passed")
else:
    print(f"test failed num1 contains {calc_page.number1_value() }")

if calc_page.number2_value() == "":
    print("test passed")
else:
    print(f"test failed num2 contains {calc_page.number2_value()}")

sleep(3)
