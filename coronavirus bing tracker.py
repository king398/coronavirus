from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get('https://www.bing.com/covid/local/india')
search = driver.find_element_by_id('maharashtra_india')  # enter your state id on bing covid-19 tracker
search.click()
states_id = ['ahmednagar_maharashtra_india', 'nanded_maharashtra_india']  # districts you want to see
total_case = []
for i in states_id:
	name_of_state = driver.find_element_by_id(i)
	name_of_state.click()
	cases = driver.find_elements_by_class_name('confirmed')
	for case in cases:
		print('{}:{}'.format(i, case.text))

time.sleep(10)
driver.quit()
