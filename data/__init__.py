def coronavirus_case(Path, state_name_element, district_id):
	from selenium import webdriver
	import time
	import locale
	total_case = {}
	driver = webdriver.Chrome(Path)
	driver.get('https://www.bing.com/covid/local/india')
	state_name = driver.find_element_by_id(state_name_element)
	state_name.click()

	locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
	for i in district_id:
		name_of_district = driver.find_element_by_id(i)
		name_of_district.click()
		cases = driver.find_elements_by_class_name('confirmed')

		for case in cases:
			case_int = locale.atoi(case.text)

			if case_int <= 17297296:  # change the value to compare with with the latest covid count
				print('{}:{}'.format(i, case.text))
				total_case.update({i: case.text})
	print(total_case)
	time.sleep(5)
	driver.quit()
