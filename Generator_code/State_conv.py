

# MAJOR ERROR ON THE SPACING IN FILE NAMES! NEEDS TO BE FIXED STILL


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
			population = "manpower = 1000"
		
		if row[4]:
			owner = f"owner = {row[4]}"													# owner
		else:
			owner = "TST"

		if row[5]: 																		# first core
			core1 = f"add_core_of = {row[5]}"
		else:
			core1 = '' 
		
		if row[6]:																		# second core
			core2 = f"add_core_of = {row[6]}"
		else:
			core2 = '' 

		if row[7]:																		# third core
			core3 = f"add_core_of = {row[7]}"
		else:
			core3 = '' 

		if row[8]:																		# Victory points (up to 3)
			vp1 = 'victory_points = {'+ f"{row[8]} 10" + '}'
		else:
			vp1 = ''
		if row[9]:																		
			vp2 = '\nvictory_points = {'+ f"{row[9]} 10" + '}'
		else:
			vp2 = ''
		if row[10]:																		
			vp3 = '\nvictory_points = {'+ f"{row[10]} 10" + '}'
		else:
			vp3 = ''

		if row[11]:																		# infrastructure
			infrastructure = f"infrastructure = {row[11]}"
		else:
			infrastructure = ''

		if row[12]:																		# Civil / industrial complex
			civil_fac = f"industrial_complex = {row[12]}"
		else:
			civil_fac = ''
		
		if row[13]:																		# mili / arms factory
			mil_fac = f"arms_factory = {row[13]}"
		else:
			mil_fac = ''

		if row[14]:																		# synthetic_refinery
			refinery = f"synthetic_refinery = {row[14]}"
		else:
			refinery = ''
		
		if row[15]:																		# dockyard
			dockyard = f"dockyard  = {row[15]}"
		else:
			dockyard = ''

		if row[16]:																		# buildings_max_level_factor
			build_factor = f"\nbuildings_max_level_factor = {row[16]}"
		else:
			build_factor = ''

		if row[17]:																		# airbase / air_base
			air_base = f"air_base  = {row[17]}"
		else:
			air_base = ''

		if row[19]:																		# navalbase / naval_base
			naval_base = f"{row[19]} = " + '{' + f"naval_base = {row[18]}" + '}'
		else:
			naval_base = ''
		
		# provinces = """provinces = {
		# 	1 2 3
		# }"""

#----------------------- WHAT IT WRITES: ------------------------#
		try:
			prefix = f"{file_id}-" 					# finds a file based on its ID
			RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
			if RightFile==[]:
				prefix = f"{file_id} - " 					# finds a file based on its ID
				RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
			print(RightFile) 						# prints the name of the file to be sure
			
			split3 = RightFile[0].split("- ")		# removes prefix from file name
			if not split3[1]:
				split3 = RightFile[0].split("-")
			
			FoundFile = split3[1].split(".")		# removes suffix from file name
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
			#the result is something in the shape "={1 2 3", which means a } has to be added to the end
			provinces = "provinces" + split2[0] + "\t}" #formats it proper

			f = open(Output+f"{row[0]}-{row[1]}.txt", 'w+') #creates (or opens) a .txt file named the id number and the name given up in the second row

			f.write(
				'state={' + f"""
		id = {file_id}
		name = "{name}"
		{population}{build_factor}

		{state_category}

		history = """ + '{' + f"""
			{owner}
			{core1}
			{core2}
			{core3}

			{vp1} {vp2} {vp3}

			buildings = """ + '{' + f"""
				{infrastructure}
				{civil_fac}
				{mil_fac}
				{dockyard}
				{refinery}
				{air_base}
				{naval_base}
		""" + '} }' +f"""
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


	



