# FOR UPDATING STRATEGIC REGION NAMES

from csv import reader
import os
import sys

#Doc = 'localisation\\strategic_region_names_l_english.yml'
Output = 'Generator_code\\Output\\'
#Source = 'history\\states\\'

print("The script has started. Please do not touch any files")

#List = [filename for filename in os.listdir(Source)]

Icon_names = 'Generator_code\\Focus_icons_names.csv'
Output = 'Generator_code\\Output\\'
Source = 'history\\states\\'

FINAL = ""

print("The script has started. Please do not touch any files")

with open(Icon_names, 'r') as datalist: 
	csv_reader = reader(datalist)		#reads the data in the file
	print("Focus_icons_names.csv has successfully been read")
	
	for row in csv_reader:				#For each row of data, we do the following:
		print(row)                		#prints

#-------------------- Determining all values --------------------#
		focus_name = row[0]	
		print (focus_name)
		
#----------------------- WHAT IT WRITES: ------------------------#
		try:
			# SpriteType = {
			# name = "GFX_focus_generic_steel"
			# texturefile = "gfx/interface/goals/focus_generic_steel.dds"			
			# }
		
			Entry = '		SpriteType = { \n		name = "GFX_' + str(focus_name) + '" \n		texturefile = "gfx/interface/goals/' + str(focus_name) + '.dds" \n		}\n'

			FINAL += Entry
		except:
			print(f"error with name '{focus_name}'!")



with open(Output+"focus_stuff.txt", 'w') as DOC:
	DOC.write(FINAL)									#writes the file
DOC.close()

print("Finished running the script")