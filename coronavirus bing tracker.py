from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get('https://www.bing.com/covid/local/india')
search = driver.find_element_by_id('maharashtra_india')  # enter your state id on bing covid-19 tracker
search.click()
states_id = ['nanded_maharashtra_india']  # districts you want to see
total_case = []
ie = 0
for i in states_id:
	name_of_state = driver.find_element_by_id(i)
	name_of_state.click()
	cases = driver.find_elements_by_class_name('confirmed')

	for case in cases:
		print('{}:{}'.format(i, case.text))
	print(ie)
	ie += 1
	print(ie)

print(ie)

time.sleep(10)
driver.quit()
