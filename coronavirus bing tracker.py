# !!!!!!!!!!!!!!!!! READ THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! this was built by mithil salunkhe. don`t read
# my commit message. please only mess with the variables i have commented unless you are god just please AND I MEAN
# IT. if you want to contribute please contribute. and don`t remove this

from selenium import webdriver
import time
import locale
start_time = time.time()


PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome


state_name = driver.find_element_by_id("maharashtra_india")  # enter your state id on bing covid-19 tracker
state_name.click()
district_id = ['nanded_maharashtra_india', 'mumbai_maharashtra_india', 'pune_maharashtra_india',
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

	ie += 1
print("--- %s seconds ---" % (time.time() - start_time))

time.sleep(5)
driver.quit()
