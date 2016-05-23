
# coding: utf-8

# In[165]:

# USE THAT ON IPYTHON NOTEBOOK
#%install_ext https://raw.github.com/cpcloud/ipython-autotime/master/autotime.py
#%load_ext autotime
#%matplotlib inline 

import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt
import pdb
import pandas as pd

df = pd.read_csv('/Users/air/Desktop/datasets/White_House_Visitor_Records_Requests.csv',
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


# In[168]:

import requests
import xml.etree.ElementTree as xmlTree
for dire in range(0,500):
    #if len(str(df.iloc[dire].NAMELAST)) == 0:
        #name.append(str(df.iloc[dire].NAMEFIRST))
    #elif len(str(df.iloc[dire].NAMEFIRST)) == 0:
        #name.append(str(df.iloc[dire].NAMELAST))
    #else:
    artistname = str(df.iloc[dire].NAMELAST) + " " + str(df.iloc[dire].NAMEFIRST)
    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist='               + artistname + '&api_key=b863970e9ba9d8391a162cae75ce422b' #&format=json'
    response = requests.get(url)
    if str(response) == '<Response [200]>':
        root = xmlTree.fromstringlist(response.content)
        ar = root.find('artist')
        print ar.find('name').text
        stats = ar.find('stats')
        print 'listners: ' + stats.find('listeners').text
        print 'playcounts: ' + stats.find('playcount').text
    #else:
    #    print 'no such musician in lastFM'
       


# In[ ]:



