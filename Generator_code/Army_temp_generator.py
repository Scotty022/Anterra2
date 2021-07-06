
import os
import sys

Tags_file = 'common\\country_tags\\00_countries.txt'
Output = 'Generator_code\\Output\\'
Source = 'history\\states\\'

print("The script has started. Please do not touch any files")

with open(Tags_file, 'r') as datalist: 
	content = datalist.readlines()
	print("00_countries has been successfully found")
	
	for row in content:				#For each row of data, we do the following:
		#print(row)                		#prints
		TAG = row[0:3]
		print(TAG)
		

#----------------------- WHAT IT WRITES: ------------------------#
		try:
			FILE_NAME = f"{TAG}_1946" 

			f = open(Output+f"{FILE_NAME}.txt", 'w+') #creates (or opens) a .txt file
			f.write(
				"""##################################
########### Templates ############
##################################
division_template = { # Infantry Division
	name = "Infantry Division" 				
	#division_names_group = TST_INF_01
	
	regiments = {
		infantry = { x = 0 y = 0 }
		infantry = { x = 0 y = 1 }
		infantry = { x = 0 y = 2 }
		infantry = { x = 1 y = 0 }
		infantry = { x = 1 y = 1 }
		infantry = { x = 1 y = 2 }
		infantry = { x = 2 y = 0 }
		infantry = { x = 2 y = 1 }
		infantry = { x = 2 y = 2 }
	}
	support = {
		artillery = { x = 0 y = 0 }
		recon = { x = 0 y = 1 }
	}
}
division_template = { # Cavalry Division
	name = "Cavalry Division" 				
	#division_names_group = TST_CAV_01
	
	regiments = {
		cavalry = { x = 0 y = 0 }
		cavalry = { x = 0 y = 1 }
		cavalry = { x = 0 y = 2 }
		cavalry = { x = 1 y = 0 }
		cavalry = { x = 1 y = 1 }
		cavalry = { x = 1 y = 2 }	
	}
}

##################################
############# Units ##############
##################################
units = {
	# division = { 
	# 	division_name = {
	# 		is_name_ordered = yes
	# 	}
	# 	location = 1213	
	# 	division_template = "Infantry Division" 
	# 	start_experience_factor = 0.4
	# 	start_equipment_factor = 0.7
	# }
}
""" 
			)
		except:
			print(f"!!! Failed writing file with tag: {TAG}")
			print(sys.exc_info())
print("- The script has ended. Thank you for using! -")


