# FOR UPDATING LOCATIONS OF AIRPORTS AND ROCKET-SITES

from csv import reader
import os
import sys

#Doc = 'localisation\\strategic_region_names_l_english.yml'
States_Raw = 'Generator_code\\States_Raw.csv'
Output = 'Generator_code\\Output\\'

print("The script has started. Please do not touch any files")

#List = [filename for filename in os.listdir(Source)]

AIRPORTS = ""
ROCKETS  = ""

with open(States_Raw, 'r') as datalist: 
	csv_reader = reader(datalist)
	print("States_Ras.csv has successfully been read")

	for row in csv_reader:	# Airfield locations
		state_ID = row[0]
		prov_ID  = row[18]
		if prov_ID == "":
			continue
		
		# 201 = { 4561 }
		Entry = str(state_ID) + " = { " + str(prov_ID) + " }\n"
		#print(Entry)

		AIRPORTS += Entry

with open(States_Raw, 'r') as datalist: 
	csv_reader = reader(datalist)
	
	for row in csv_reader:	# Rocket site locations
		state_ID = row[0]
		prov_ID  = row[19]
		if prov_ID == "":
			continue

		Entry = str(state_ID) + " = { " + str(prov_ID) + " }\n"
		#print(Entry)

		ROCKETS += Entry

with open(Output+"airports.txt", 'w') as DOC:
	DOC.write(AIRPORTS)									#writes the file
DOC.close()

with open(Output+"rocketsites.txt", 'w') as DOC:
	DOC.write(ROCKETS)									#writes the file
DOC.close()

print("- The script has ended. Thank you for using! -")
