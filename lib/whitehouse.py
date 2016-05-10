import numpy as np
import pandas as pd

class WhiteHouse:
	def __init__(self, datasetlocation, nrows=0):
		if (nrows == 0):
			self.df = pd.read_csv(datasetlocation,
	            parse_dates=['APPT_START_DATE'], 
	            dayfirst=True,
	            usecols=['NAMELAST', 'NAMEFIRST', 'APPT_START_DATE']) # reads only these columns to memory
		else:
			self.df = pd.read_csv('../datasets/White_House_Visitor_Records_Requests.csv',
                    parse_dates=['APPT_START_DATE'], 
                    dayfirst=True,
                    usecols=['NAMELAST', 'NAMEFIRST', 'APPT_START_DATE'], # reads only these columns to memory
                    nrows=10000) # for faster testing, remove for efective use of the dataframe

	def getVisits(self, firstname, lastname):
		has_first_name = self.df['NAMEFIRST'] == firstname.upper()
		has_last_name = self.df['NAMELAST'] == lastname.upper()
		return self.df[has_last_name & has_first_name]

	def hasVisits(self, firstname, lastname):
		return (len(self.getVisits(firstname, lastname)) > 0)

if __name__ == "__main__":
	WH = WhiteHouse('../datasets/White_House_Visitor_Records_Requests.csv', nrows = 1000)
	print ('Visits from JIITU ABRAHAM:')
	print (WH.getVisits('JIITU', 'ABRAHAM'))
	print ('---')
	print ('Visits from JiItU AbRaHaM:')
	print (WH.getVisits('JiItU', 'AbRaHaM'))
	print ('---')
	print ('Visits from Rafael Peres:')
	print (WH.getVisits('RAFAEL', 'PERES'))
	print ('---')
	print ('Has visits from Rafael Peres?')
	print (WH.hasVisits('RAFAEL', 'PERES'))
	print ('---')
	print ('Has visits from JiItU AbRaHaM?')
	print (WH.hasVisits('JiItU', 'AbRaHaM'))
	print ('---')
	print ('Example from dataset:')
	print (WH.df[:10])