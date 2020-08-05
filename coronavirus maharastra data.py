# !!!!!!!!!!!!!!!!! READ THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! this was built by mithil salunkhe. don`t read
# my commit message. please only mess with the variables i have commented unless you are god just please AND I MEAN
# IT. if you want to contribute please contribute. and don`t remove thi
from selenium import webdriver
import time
import locale
from xlwt import Workbook
import datetime

start_time = time.time()


def coronavirus_case(path, state_name_element, district_id):
	total_case = {}
	driver = webdriver.Chrome(path)
	driver.get('https://www.bing.com/covid/local/india')
	time.sleep(5)
	state_name = driver.find_element_by_id(state_name_element)
	state_name.click()

	locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
	for i in district_id:
		name_of_district = driver.find_element_by_id(i)
		name_of_district.click()
		cases = driver.find_elements_by_class_name('confirmed')
		more_infromation = driver.find_elements_by_class_name('total')
		for_more = {}
		info_about_what_they_are = driver.find_elements_by_class_name('description')
		for more, info in zip(more_infromation, info_about_what_they_are):
			print(more.text, info.text)
			for_more.update({info.text: more.text})

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
			writing_int = locale.atoi(writing)
			sheet1.write(ie, 1, writing_int)
			ie += 1

		excelfile.save(
			"sample-maharashtra.xls")  # enter the name of the file in the quotation marks

		time.sleep(5)
		driver.quit()
		print(for_more)

	districst_id = ['nanded_maharashtra_india', 'mumbai_maharashtra_india', 'pune_maharashtra_india',
	                'thane_maharashtra_india', 'raigarh_maharashtra_india',
	                'nashik_maharashtra_india', 'palghar_maharashtra_india',
	                'nashik_maharashtra_india', 'aurangabad_maharashtra_india', 'solapur_maharashtra_india',
	                'kolhapur_maharashtra_india', 'nagpur_maharashtra_india',
	                'ahmednagar_maharashtra_india', 'satara_maharashtra_india',
	                'dhule_maharashtra_india', 'akola_maharashtra_india',
	                'sangli_maharashtra_india',
	                'amravati_maharashtra_india',
	                'latur_maharashtra_india',
	                'jalna_maharashtra_india',
	                'ratnagiri_maharashtra_india',
	                'buldana_maharashtra_india',
	                'osmanabad_maharashtra_india', 'yavatmal_maharashtra_india',
	                'beed_maharashtra_india', 'parbhani_maharashtra_india',
	                'nandurbar_maharashtra_india', 'washim_maharashtra_india',
	                'hingoli_maharashtra_india', 'chandrapur_maharashtra_india',
	                'sindhudurg_maharashtra_india', 'gondia_maharashtra_india',
	                'gadchiroli_maharashtra_india', 'bhandara_maharashtra_india',
	                'wardha_maharashtra_india']  # districts you want to see


coronavirus_case(path="C:\Program Files (x86)\chromedriver.exe", state_name_element="maharashtra_india",
                 district_id=districst_id)
print("--- %s seconds ---" % (time.time() - start_time))
