from csv import reader

States_Raw = 'Generator_code\\States_Raw.csv'
Output = 'Generator_code\\Output\\'

with open(States_Raw, 'r') as datalist: 
	csv_reader = reader(datalist)		#reads the data in the file
	for row in csv_reader:				#For each row of data, we do the following:
		print(row)                		#prints

#-------------------- Determining all values --------------------#
		file_id = row[0]																# id
		name = row[1]																	# name
		state_category = f"state_category = {row[2]}"									# state_category
		population = f"manpower = {row[3]}"												# population/manpower
		owner = f"owner = {row[4]}"														# owner

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
			victory_points = 'victory_points = {'+ f"{row[8]} {row[9]} {row[10]}" + '}'
		else:
			victory_points = ''
		
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

		if row[15]:																		# buildings_max_level_factor
			build_factor = f"buildings_max_level_factor = {row[15]}"
		else:
			build_factor = ''

		if row[16]:																		# airbase / air_base
			air_base = f"air_base  = {row[16]}"
		else:
			air_base = ''

		if row[18]:																		# navalbase / naval_base
			naval_base = f"{row[18]} = " + '{' + f"naval_base = {row[17]}" + '}'
		else:
			naval_base = ''
		
		provinces = """provinces = {
			1 2 3
		}"""
		


		f = open(Output+f"{row[0]}-{row[1]}.txt", 'w+') #creates (or opens) a .txt file named the id number and the name given up in the second row
# #----------------------- WHAT IT WRITES: ------------------------#
		f.write(
			'state={' + f"""
		id = {file_id}
		name = "STATE_{file_id}" #{name}
		{population}
		{build_factor}

		{state_category}

		history = """ + '{' + f"""
			{owner}
			{core1}
			{core2}
			{core3}

			{victory_points}

			buildings = """ + '{' + f"""
				{infrastructure}
				{civil_fac}
				{mil_fac}
				{refinery}
				{air_base}
				{naval_base}
		""" + '} }' +f"""
		{provinces}
""" + '}'
		)
# 		f.write('state={' + f""" 
#  		id = {row[0]}
# 		name = "STATE_{row[0]}" # {row[1]}
# 		manpower = {row[3]}
# 		state_category = "{row[2]}"

# 		history=""" + '{' + f"""
# 			owner = {row[4]}
# 			victory_points = {victory_points} 
# 			buildings =""" + '{' + f"""
# 				infrastructure = {row[11]}
# 				industrial_complex = {row[12]}
# 				arms_factory = {row[13]}
# 				airbase = {row[]}
# 		""" + '}}}')

# 		#f = open(Output + f'{row[0]}-{row(1)}.txt', 'w+') 
# 		#f.write("state={" + f"""br/
# 		#id = {row[0]}
# 		#name = "STATE_{row[0]}" # {row[1]}
# 		#manpower = {row[3]}
# 		#""" + '}')


	



