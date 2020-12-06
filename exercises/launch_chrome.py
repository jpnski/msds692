import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.google.com')
input('Press any key to quit')

driver.quit()
