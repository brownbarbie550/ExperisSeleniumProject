from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#create a browser object (open the browser)
driver = webdriver.Chrome()

#go to the required URL
driver.get("https://www.advantageonlineshopping.com/#/")

#maximize the window
driver.maximize_window()

#define a timeout: in case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

#click on speakers category
speakers = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
speakers.click()

#click on a specific speaker
driver.find_element(By.CSS_SELECTOR, r"#\32 5").click()#r is useful in such cases where we have \ signs


#choose color
# driver.find_element(By.CSS_SELECTOR, "#bunny").click()
driver.find_element(By.CSS_SELECTOR, "span[title='BLACK'][id='bunny']").click()

#change quantity to 5
# quantity= driver.find_element(By.CSS_SELECTOR, "#productProperties > div.smoolMargin > e-sec-plus-minus > div > div:nth-child(2) > input")
quantity= driver.find_element(By.CSS_SELECTOR, "[name='quantity']")
# quantity.clear() #a command to clear fields or text box, not in this case because the field can't be empty
quantity.send_keys(Keys.BACKSPACE+"5")
# quantity.send_keys("5")

#display the name and price of the product
name_element = driver.find_element(By.CSS_SELECTOR, "#Description > h1")
print(f"product name:{name_element.text}")

price_element = driver.find_element(By.CSS_SELECTOR, "#Description > h2")
print(f"product price:{price_element.text}")

#click on add to cart button
driver.find_element(By.CSS_SELECTOR, "#productProperties > div.fixedBtn > button").click()

sleep(10)

