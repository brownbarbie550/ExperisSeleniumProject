from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


#create a browser object (open the browser)
driver1 = webdriver.Chrome()

#go to the required URL
driver1.get("https://demo.guru99.com/test/newtours/reservation.php")

#maximize the window
driver1.maximize_window()

#define a timeout: in case an element is not found - wait 10 seconds
driver1.implicitly_wait(10)


sleep(10)






#check radio button status (round trip - on, one way)