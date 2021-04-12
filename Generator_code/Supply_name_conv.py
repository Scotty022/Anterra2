# FOR UPDATING STRATEGIC REGION NAMES

import os
import sys

#Doc = 'localisation\\strategic_region_names_l_english.yml'
Output = 'Generator_code\\Output\\'
Source = 'map\\supplyareas\\'

print("The script has started. Please do not touch any files")

List = [filename for filename in os.listdir(Source)]

TXT = "ï»¿l_english: \n"

for region in List:
	#with open(Source+region,'r') as Cont:
	#	NAME = Cont.read().split('"')[1]
	#	print(NAME)

	ID = region.split("-",1)[0]
	Pre_NAME = region.split("-",1)[1]
	NAME = Pre_NAME.split(".")[0]
	#STRATEGICREGION_4:0 "Ireland"
	Entry = f' SUPPLYAREA_{ID}:0 "{NAME}" \n'
	print(Entry)

	TXT += Entry

with open(Output+"supply_area_names_l_english.yml", 'w') as DOC:
	DOC.write(TXT)
DOC.close()

print("- The script has ended. Thank you for using! -")
