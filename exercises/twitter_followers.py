from login import login
import time
from selenium import webdriver

u,p = login()

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('http://www.twitter.com/login')
time.sleep(1.5)

ufield = driver.find_element_by_css_selector("input[type='text']")
ufield.send_keys(u)

pfield = driver.find_element_by_css_selector("input[type='password']")
pfield.send_keys(p)
pfield.submit()

driver.get('https://twitter.com/DataInstituteSF/following')
time.sleep(2)

driver.execute_script("window.scrollTo(0, 10000);") # scroll down
time.sleep(2)

driver.execute_script("window.scrollTo(0, 10000);") # scroll down more
time.sleep(2)

links = driver.find_elements_by_xpath('//a[@role="link"]')
links = [(link.get_attribute("href"),link.text) for link in links if '@' in link.text]
print(links)

input("Press Enter to quit")

driver.quit()
