# FOR UPDATING LOCATIONS OF AIRPORTS AND ROCKET-SITES

from csv import reader
import os
import sys

#Doc = 'localisation\\strategic_region_names_l_english.yml'
States_Raw = 'Generator_code\\States_Raw.csv'
Output = 'Generator_code\\Output\\'
State_Folder = 'history\\states\\'

print("The script has started. Please do not touch any files")

#List = [filename for filename in os.listdir(Source)]

AIRPORTS = ""
ROCKETS  = ""

with open(States_Raw, 'r') as datalist: 
	csv_reader = reader(datalist)
	print("States_Raw.csv has successfully been read")

	for row in csv_reader:	# Airfield locations
		state_ID = row[0]
		prov_ID  = row[18]

		# if int(state_ID) > 50:
		# 	continue

		if prov_ID == "":
			#continue

			#Find the state file
			try:
				prefix = f"{state_ID}-" 					# finds a file based on its ID
				RightFile = [filename for filename in os.listdir(State_Folder) if filename.startswith(prefix)]
				#print("a: "+str(RightFile)) 
			except:
				print(f"!!! attempting to find ID {state_ID} has failed")
				print(sys.exc_info())	
			
			print(state_ID)
			#open file
			g = open(State_Folder+RightFile[0], "r")	# opens the OG file
			split1 = g.read().split("provinces={")		# cuts the file after 'provinces'
			split2 = split1[1].split("\n")
			split3 = split2[1].split("}", 1) 			# limits the file to only the province numbers
			provinces = split3[0].split(" ")			# formats it proper to a list
			g.close()

			cleaned = [] # provinces #[province for province in provinces if province.startswith('\n')]

			#any(char.isdigit() for char in inputString)
			for ENTRY in provinces:
				if any(char.isdigit() for char in ENTRY):
					cleaned.append(ENTRY)

			print(cleaned)

			# Because of inregularity of spaces used in declaring provinces (sometimes there is one
			# right after "provinces={" or at the start of the list of numbers), first an attempt is 
			# made on trying to get the third entry. However, because some states have less than 3 
			# provinces, attemps will be made on fetching the 2nd if the 3rd fails. Idem for the
			# fetching the first entry in the provinces list. This is really 'beun', but that is how
			# life be sometimes. Besides, this is not a critical code, just some assistant in changing
			# very very lorge files :)
			try:
				if cleaned[2] != "" :
					prov_ID = cleaned[2]
				else:
					prov_ID = cleaned[1]
			except:
				prov_ID = cleaned[0]
			 
			Entry = str(state_ID) +  " = { " + str(prov_ID) + " }\n"
		else:
			# 201 = { 4561 }
			Entry = str(state_ID) + " = { " + str(prov_ID) + " }\n"
		#print(Entry)

		AIRPORTS += Entry

print ("SECOND SECTION -------------------------------------------------------")

with open(States_Raw, 'r') as datalist: 
	csv_reader = reader(datalist)
	
	for row in csv_reader:	# Rocket site locations
		state_ID = row[0]
		prov_ID  = row[19]

		# if int(state_ID) > 50:
		# 	continue

		if prov_ID == "":
			#continue

			#Find the state file
			try:
				prefix = f"{state_ID}-" 					# finds a file based on its ID
				RightFile = [filename for filename in os.listdir(State_Folder) if filename.startswith(prefix)]
				#print("a: "+str(RightFile)) 
			except:
				print(f"!!! attempting to find ID {state_ID} has failed")
				print(sys.exc_info())	
			
			#open file
			g = open(State_Folder+RightFile[0], "r")	# opens the OG file
			split1 = g.read().split("provinces={")		# cuts the file after 'provinces'
			split2 = split1[1].split("\n")
			split3 = split2[1].split("}", 1) 			# limits the file to only the province numbers
			provinces = split3[0].split(" ")			# formats it proper to a list
			g.close()

			cleaned = [] # provinces #[province for province in provinces if province.startswith('\n')]

			#any(char.isdigit() for char in inputString)
			for ENTRY in provinces:
				if any(char.isdigit() for char in ENTRY):
					cleaned.append(ENTRY)

			print(cleaned)

			# Because of inregularity of spaces used in declaring provinces (sometimes there is one
			# right after "provinces={" or at the start of the list of numbers), first an attempt is 
			# made on trying to get the third entry. However, because some states have less than 3 
			# provinces, attemps will be made on fetching the 2nd if the 3rd fails. Idem for the
			# fetching the first entry in the provinces list. This is really 'beun', but that is how
			# life be sometimes. Besides, this is not a critical code, just some assistant in changing
			# very very lorge files :)
			try:
				if cleaned[4] != "" :
					prov_ID = cleaned[4]
				elif cleaned[2] != "":
					prov_ID = cleaned[2]
				else:
					prov_ID = cleaned[0]
			except:
				prov_ID = cleaned[0]
			 
			Entry = str(state_ID) +  " = { " + str(prov_ID) + " }\n"
		else:
			# 201 = { 4561 }
			Entry = str(state_ID) + " = { " + str(prov_ID) + " }\n"

		ROCKETS += Entry

with open(Output+"airports.txt", 'w') as DOC:
	DOC.write(AIRPORTS)									#writes the file
DOC.close()

with open(Output+"rocketsites.txt", 'w') as DOC:
	DOC.write(ROCKETS)									#writes the file
DOC.close()

print("- The script has ended. Thank you for using! -")
