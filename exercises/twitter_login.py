from login import login
import time
from selenium import webdriver

u,p = login()

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('http://twitter.com/login')
time.sleep(0.75)

ufield = driver.find_element_by_css_selector("input[type='text']")
ufield.send_keys(u)

pfield = driver.find_element_by_css_selector("input[type='text']")
pfield.send_keys(p)

pfield.submit()

input('Press Enter key to quit')

driver.quit()
