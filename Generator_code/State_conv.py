# Set limit on what range to generate
LimitL = 200
LimitU = 400

from csv import reader
import os
import sys

States_Raw = 'Generator_code\\States_Raw.csv'
Output = 'Generator_code\\Output\\'
Source = 'history\\states\\'

print("The script has started. Please do not touch any files")

with open(States_Raw, 'r') as datalist: 
	csv_reader = reader(datalist)		#reads the data in the file
	print("States_Ras.csv has successfully been read")
	
	for row in csv_reader:				#For each row of data, we do the following:
		#print(row)                		#prints

		if int(row[0]) < LimitL: 		#Skips all entries that are either lower than LimitL or higher than LimitU
			continue
		if int(row[0]) > LimitU:
			continue

#-------------------- Determining all values --------------------#
		file_id = row[0]																# id
		name = row[1]																	# name
		if row[2]:
			state_category = f"state_category = {row[2]}"								# state_category
		else:
			state_category = "state_category = pastoral"
		if row[3]:
			population = f"manpower = {row[3]}"											# population/manpower
		else:
			population = "manpower = 100000"
		
		if row[4]:
			owner = f"owner = {row[4]}"													# owner
		else:
			owner = "TST"

		if row[5]: 																		# first core
			core1 = f"add_core_of = {row[5]}"
		else:
			core1 = '' 
		
		if row[6]:																		# second core
			core2 = f"\n			add_core_of = {row[6]}"
		else:
			core2 = '' 

		if row[7]:																		# third core
			core3 = f"\n			add_core_of = {row[7]}"
		else:
			core3 = '' 

		if row[8]:																		# Victory points (up to 3)
			vp1 = 'victory_points = {'+ f"{row[8]} 10" + '}'
		else:
			vp1 = ''
		if row[9]:																		
			vp2 = '\n			victory_points = {'+ f"{row[9]} 10" + '}'
		else:
			vp2 = ''
		if row[10]:																		
			vp3 = '\n			victory_points = {'+ f"{row[10]} 10" + '}'
		else:
			vp3 = ''

		if row[11]:																		# infrastructure
			infrastructure = f"\n				infrastructure = {row[11]}"
		else:
			infrastructure = ''

		if row[12]:																		# Civil / industrial complex
			civil_fac = f"\n				industrial_complex = {row[12]}"
		else:
			civil_fac = ''
		
		if row[13]:																		# mili / arms factory
			mil_fac = f"\n				arms_factory = {row[13]}"
		else:
			mil_fac = ''

		if row[14]:																		# synthetic_refinery
			refinery = f"\n				synthetic_refinery = {row[14]}"
		else:
			refinery = ''
		
		if row[15]:																		# dockyard
			dockyard = f"\n				dockyard  = {row[15]}"
		else:
			dockyard = ''

		if row[16]:																		# buildings_max_level_factor
			build_factor = f"\n		buildings_max_level_factor = {row[16]}"
		else:
			build_factor = ''

		if row[17]:																		# airbase / air_base
			air_base = f"\n				air_base  = {row[17]}"
		else:
			air_base = ''

		if row[21]:																		# navalbase / naval_base
			naval_base = f"\n				{row[21]} = " + '{' + f"naval_base = {row[20]}" + '}'
		else:
			naval_base = ''
		
		if row[22] or row[23] or row[24] or row[25] or row[26] or row[27]:				# Resources section
			if row[22]:	
				steel = f'\n			steel = {row[22]}'
			else:
				steel = ''

			if row[23]:	
				aluminium = f'\n			aluminium = {row[23]}'
			else:
				aluminium = ''

			if row[24]:	
				rubber = f'\n			rubber = {row[24]}'
			else:
				rubber = ''

			if row[25]:	
				tungsten = f'\n			tungsten = {row[25]}'
			else:
				tungsten = ''
			
			if row[26]:	
				chromium = f'\n			chromium = {row[26]}'
			else:
				chromium = ''

			if row[27]:	
				oil = f'\n			oil = {row[27]}'
			else:
				oil = ''
			
			resources = '\n		resources = {' + f"{steel}{aluminium}{rubber}{tungsten}{chromium}{oil}"+"\n		}" 
		else:
			resources = ''
		
		# provinces = """provinces = {
		# 	1 2 3
		# }"""

#----------------------- WHAT IT WRITES: ------------------------#
		try:
			prefix = f"{file_id}-" 					# finds a file based on its ID
			RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
			#print("a: "+str(RightFile)) 
			if RightFile==[]:
				prefix = f"{file_id} - " 					# finds a file based on its ID
				RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
			print("b: "+str(RightFile)) 						# prints the name of the file to be sure
			
			# This sections removes the prefix from the file name. First
			# by removing the one with a space and then the one without.
			# The second statement uses '-1' for an indentifier. It will
			# use the last entry of the list, which means regardless if
			# it is already split, it can process the entry correctly.
			split3 = RightFile[0].split("- ")		
			split4 = split3[-1].split("-")			

			FoundFile = split4[-1].split(".")		# removes suffix from file name
			if name != FoundFile[0]:				# checks of the stripped file name matches the new name, otherwise give errors
				if FoundFile[0] == 'txt':
					print(f"! The OG file didnt have a name (pushed file has name: {name})")
				if not name:
					print(f"! The new file has no name specified (pulled name was: {FoundFile[0]})")
				else:
					print(f"! The file pulled and pushed have different names ({FoundFile[0]} pulled, {name} pushed). You might want to double check the names")
			
			g = open(Source+RightFile[0], "r")		#opens the OG file
			split1 = g.read().split("provinces")		#cuts the file after 'provinces'
			split2 = split1[1].split("}", 1) 			#picks the second half and cuts on the first } it finds
			#the result is something in the shape "={\n1 2 3", which means a } has to be added to the end
			provinces = "provinces" + split2[0] + "}" #formats it proper

			f = open(Output+f"{row[0]}-{row[1]}.txt", 'w+') #creates (or opens) a .txt file named the id number and the name given up in the second row

			f.write(
				'state={' + f"""
		id = {file_id}
		name = "{name}"
		{population}
		{state_category}{build_factor}{resources}

		history = """ + '{' + f"""
			{owner}
			{core1}{core2}{core3}

			{vp1}{vp2}{vp3}

			buildings = """ + '{' + f"""
				{infrastructure}{civil_fac}{mil_fac}{dockyard}{refinery}{air_base}{naval_base}
			""" + """} 
		}""" + f"""
		{provinces}
""" + '}'
			)
		except IndexError:
			if prefix == "id-":
				print('! The display of this "error" is triggered by the header of the .csv file. If no further error messages show up, everything is fine.')
			else:
				print(f"!!! The ID {file_id} name could not be found! There might be a file missing.")
		except:
			print(f"!!! attempting to find/create ID {file_id} ({name}) has failed")
			print(sys.exc_info())
print("- The script has ended. Thank you for using! -")


