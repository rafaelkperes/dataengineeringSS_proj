# USE THAT ON IPYTHON NOTEBOOK
#%install_ext https://raw.github.com/cpcloud/ipython-autotime/master/autotime.py
#%load_ext autotime
#%matplotlib inline 

import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt
import pdb
import pandas as pd

df = pd.read_csv('../datasets/White_House_Visitor_Records_Requests.csv',
                    parse_dates=['APPT_START_DATE'], 
                    dayfirst=True,
                    #index_col=['NAMELAST','NAMEFIRST'],
                    usecols=['NAMELAST', 'NAMEFIRST', 'APPT_START_DATE'], # reads only these columns to memory
                    nrows=10000) # for faster testing, remove for efective use of the dataframe
pd.set_option('large_repr', 'info') # will show dataframe summary

#pd.to_datetime(df['APPT_START_DATE'], format='%Y-%m-%d')
df['APPT_START_DATE'] = df['APPT_START_DATE'].apply(pd.datetools.normalize_date) # removes the hour

print ('Summary:')
print (df)
print ('Example data:')
print (df[:10])

visit_counts = df['APPT_START_DATE'].value_counts()
visit_counts[:10].plot()

has_last_name = df['NAMELAST'] == "ABRAHAM"
has_first_name = df['NAMEFIRST'] == "JIITU"
print ("Number of visits from JIITU ABRAHAM: ")
print (len(df[has_last_name & has_first_name]))

has_last_name = df['NAMELAST'] == "PERES"
has_first_name = df['NAMEFIRST'] == "RAFAEL"
print ("Number of visits from RAFAEL PERES: ")
print (len(df[has_last_name & has_first_name]))