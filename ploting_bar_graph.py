import pandas as pd
import matplotlib.pyplot as plt

execel_file = pd.read_excel(r'coronavirus\sample-maharashtra.xls')
execel_file.to_csv(r'coronavirus\sample-maharashtra.csv')
