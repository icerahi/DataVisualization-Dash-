import pandas as pd

date = list(pd.read_csv('SynesisIT.csv',sep=";")['Date'])
total_current = list(pd.read_csv('SynesisIT.csv',sep=";")['sum_of_line_currents'])[:10]
total_power = list(pd.read_csv('SynesisIT.csv',sep=";")['total_system_power'])[:10]

power_factor = list(pd.read_csv('SynesisIT.csv',sep=";")['total_system_power_factor'])[:10]

print(date,total_current,total_power,power_factor)
