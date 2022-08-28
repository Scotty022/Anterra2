# FOR UPDATING STRATEGIC REGION NAMES

import os
import sys

#Doc = 'localisation\\strategic_region_names_l_english.yml'
Output = 'Generator_code\\Output\\'
Source = 'history\\states\\'

print("The script has started. Please do not touch any files")

List = [filename for filename in os.listdir(Source)]

TXT = "ï»¿l_english: \n"

for region in List:
	#with open(Source+region,'r') as Cont:
	#	NAME = Cont.read().split('"')[1]
	#	print(NAME)

	ID = region.split("-",1)[0]
	Pre_NAME = region.split("-",1)[1]
	DISP_NAME = Pre_NAME.split(".")[0]

	if " " in DISP_NAME:
		PROG_NAME = DISP_NAME.replace(" ", "_")
	else:
		PROG_NAME = DISP_NAME

	#West_Amomosean_Islands:0 "West Amomosean Islands" # STATE_214
	Entry = f' {PROG_NAME}:0 "{DISP_NAME}" # STATE_{ID}\n'
	print(Entry)

	TXT += Entry

with open(Output+"state_names_l_english.yml", 'w') as DOC:
	DOC.write(TXT)
DOC.close()

print("- The script has ended. Thank you for using! -")
