import time
from selenium import webdriver

query = 'USF Data Science'

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.google.com')

search_box = driver.find_element_by_name('q')
search_box.send_keys(query)
search_box.submit()

input('Press Enter key to quit')

driver.quit()
