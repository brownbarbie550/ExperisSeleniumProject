from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from random import randint


driver = webdriver.Chrome()
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.maximize_window()
driver.implicitly_wait(10)

#get pets categories list
pets_list = driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a")
pets_list[1].click()


# dogs = driver.find_element(By.CSS_SELECTOR, "#SidebarContent>a")
# dogs.click()
# dogs = driver.find_element(By.XPATH, "//*[@id='SidebarContent']/a[2]")
# dogs.click()


#find the poodle and click on it
table = driver.find_element(By.TAG_NAME, "table")
tr_s = table.find_elements(By.TAG_NAME, "tr")
for tr in tr_s[1:]:
    td_s = tr.find_elements(By.TAG_NAME, "td")
    if td_s[1].text == "Poodle":
        td_s[0].click()
        break

#exercise
#choose bird
home_page = driver.find_element(By.XPATH, "//*[@id='LogoContent']/a")
home_page.click()
sleep(1)
birds = driver.find_element(By.XPATH, "//*[@id='SidebarContent']/a[5]")
birds.click()
sleep(1)
table = driver.find_element(By.TAG_NAME, "table")
tr_s = table.find_elements(By.TAG_NAME, "tr")
for tr in tr_s[1:]:
    td_s = tr.find_elements(By.TAG_NAME, "td")
    if td_s[1].text == "Amazon Parrot":
        td_s[0].click()
        break
sleep(1)
# <a href="/actions/Cart.action?addItemToCart=&amp;workingItemId=EST-18" class="Button">Add to Cart</a>
#click on add to cart
driver.find_element(By.CLASS_NAME, "Button").click()
sleep(1)
#click on quantity field
quantity = driver.find_element(By.NAME, "EST-18")
quantity.send_keys(Keys.BACKSPACE+"4")
sleep(1)
#click on update cart button
update = driver.find_element(By.NAME, "updateCartQuantities")
update.click()
sleep(1)
#back to home screen
home_page = driver.find_element(By.XPATH, "//*[@id='LogoContent']/a")
home_page.click()
sleep(3)



#choose fish
fishes = driver.find_element(By.XPATH, "//*[@id='SidebarContent']/a[1]")
fishes.click()
sleep(3)
table = driver.find_element(By.TAG_NAME, "table")
tr_s = table.find_elements(By.TAG_NAME, "tr")
for tr in tr_s[1:]:
    td_s = tr.find_elements(By.TAG_NAME, "td")
    if td_s[1].text == "Goldfish":
        td_s[0].click()
        break
sleep(3)
#click on add to cart
driver.find_element(By.CLASS_NAME, "Button").click()
sleep(3)
#click on quantity field
quantity = driver.find_element(By.NAME, "EST-20")
quantity.send_keys(Keys.BACKSPACE+"4")
sleep(3)
#click on update cart button
update = driver.find_element(By.NAME, "updateCartQuantities")
update.click()


# if list_price * quantity == total print(total approved) else print (wrong calculation)
#if goldfish total + parrot total == subtotal print(subtotal approved)
list_price = driver.find_element(By.XPATH,"//*[@id='Cart']/form/table/tbody/tr[2]/td[6]")
fish_quantity = driver.find_element(By.NAME, "EST-20")
total_price = driver.find_element(By.XPATH,"//*[@id='Cart']/form/table/tbody/tr[2]/td[7]")

list_price_text = list_price.text.strip().replace("$", "").replace(",", "")  # Remove currency and commas
list_price_value = float(list_price_text)

fish_quantity_value = int(fish_quantity.get_attribute("value").strip())

total_price_text = total_price.text.strip().replace("$", "").replace(",", "")  # Remove currency and commas
total_price_value = float(total_price_text)

expected_total = list_price_value * fish_quantity_value
if expected_total == total_price_value:
    print("total approved")
else:
    print("wrong calculation")





#if total cost + total cost == subtotal print(subtotal approved) else print(wrong calculation)
total_fish = driver.find_element(By.XPATH, "//*[@id='Cart']/form/table/tbody/tr[2]/td[7]")
total_fish_text = total_fish.text.strip().replace("$", "").replace(",", "")
total_fish_value = float(total_fish_text)

total_bird = driver.find_element(By.XPATH, "//*[@id='Cart']/form/table/tbody/tr[3]/td[7]" )
total_bird_text = total_bird.text.strip().replace("$", "").replace(",", "")
total_bird_value = float(total_bird_text)

sub_total = driver.find_element(By.XPATH, "//*[@id='Cart']/form/table/tbody/tr[4]/td[1]")
sub_total_text = sub_total.text.strip().replace("$", "").replace(",", "")
print(f"Extracted subtotal text: '{sub_total_text}'")# Debugging step
# Extract first numeric value from text
sub_total_value = next((float(word) for word in sub_total_text.split() if word.replace(".", "").isdigit()), None)
sub_total_value1 = float(sub_total_value)
print(f"Converted subtotal: {sub_total_value}")

sum_total = total_fish_value + total_bird_value
if sum_total == sub_total_value:
    print("sub total approved")
else:
    print("wrong calculation")

sleep(10)