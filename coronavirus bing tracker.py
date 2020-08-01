# !!!!!!!!!!!!!!!!! READ THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! this was built by mithil salunkhe. don`t read
# my commit message. please only mess with the variables i have commented unless you are god just please AND I MEAN
# IT. if you want to contribute please contribute. and don`t remove this

from coronavirus.data import coronavirus_case

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

coronavirus_case(Path="C:\Program Files (x86)\chromedriver.exe", state_name_element="maharashtra_india",
                 district_id=district_id)
