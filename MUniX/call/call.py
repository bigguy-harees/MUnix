import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import sys

number = sys.argv[1]


#chrome_options = Options()
#chrome_options.add_argument("--disable-user-media-security=true")



chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")





# Using Chrome to access web
driver = webdriver.Chrome( chrome_options=chrome_options)


# Open the website
driver.get('http://www.spytox.com')


#initial wait for the webpage to load
time.sleep(5)
# Find the call option
id_box = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/label[4]/span")
id_box.click() #choose the above button


time.sleep(5)
num_box=driver.find_element_by_id("phone_number")

#wait time v.v.v important
time.sleep(3)

#call code

India= driver.find_element_by_class_name("country-dropdown")
selected_text = Select(India)
selected_text.select_by_visible_text("India")

#wait time #needed
time.sleep(3)

#get keys and send to the number text box
num_box.send_keys(number)

#call button
driver.find_element_by_xpath("//*[@id='btncall']").click()

print("success")
print("success!!!!!")

# Send id information
#id_box.send_keys('1PE17cs0')


# Find login button
#login_button = driver.find_element_by_name('submit')
# Click login
#login_button.click()
