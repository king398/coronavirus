from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get('https://www.covid19india.org/state/MH')

districts = driver.find_elements_by_tag_name("path")
action = ActionChains(driver)


for district in districts:
	print(district)
	action.move_to_element(district)
	io = driver.find_element_by_class_name('district confirmed')
	print(io.text)


driver.quit()
