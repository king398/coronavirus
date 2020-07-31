from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get('https://www.bing.com/covid/local/india')
search = driver.find_element_by_id('maharashtra_india')  # enter your state id on bing covid tracker
search.click()
states_id = ['ahmednagar_maharashtra_india']
total_case = []
for i in states_id:
	name_of_state = driver.find_element_by_id(i)
	name_of_state.click()
	cases = driver.find_elements_by_class_name('confirmed')
	for case in cases:
		print(case.text)

time.sleep(10)
driver.quit()
