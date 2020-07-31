from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get('https://www.bing.com/covid/local/india')

search = driver.find_element_by_id('andhrapradesh_india')

search.click()


time.sleep(10)
driver.quit()
