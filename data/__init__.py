def coronavirus_case(Path, state_name_element, district_id):
	from selenium import webdriver
	import time
	import locale
	import xlwt
	from xlwt import Workbook
	total_case = {}
	case_1 = []
	case_2 = []
	driver = webdriver.Chrome(Path)
	driver.get('https://www.bing.com/covid/local/india')
	time.sleep(5)
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
	case_1 = total_case.keys()
	case_2 = total_case.values()

	excelfile = Workbook()
	sheet1 = excelfile.add_sheet("sheet1")
	i = 0
	ie = 0
	for writingnames in case_1:
		sheet1.write(i, 0, writingnames)

		i += 1
	for writing in case_2:
		sheet1.write(ie, 1, writing)
		ie += 1
	filename = time.time()

	excelfile.save("sample{}.xls".format(filename))  # enter the name of the file in the quotation marks

	time.sleep(5)
	driver.quit()
