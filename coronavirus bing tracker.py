# !!!!!!!!!!!!!!!!! READ THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! this was built by mithil salunkhe. don`t read
# my commit message. please only mess with the variables i have commented unless you are god just please AND I MEAN
# IT. if you want to contribute please contribute. and don`t remove this

from selenium import webdriver
import time
import locale

PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get('https://www.bing.com/covid/local/india')
time.sleep(10)
state_name = driver.find_element_by_id("maharashtra_india")  # enter your state id on bing covid-19 tracker
state_name.click()
district_id = ['nanded_maharashtra_india']  # districts you want to see
total_case = []
ie = 0
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

for i in district_id:
	name_of_state = driver.find_element_by_id(i)
	name_of_state.click()
	cases = driver.find_elements_by_class_name('confirmed')

	for case in cases:
		case_int = locale.atoi(case.text)

		if case_int <= 17297296:  # change the value to compare with with the latest covid count
			print('{}:{}'.format(i, case.text))
	print(ie)
	ie += 1
	print(ie)

print(ie)

time.sleep(10)
driver.quit()
