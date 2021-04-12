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

		
		prefix = f"{file_id}-" 					# finds a file based on its ID
		RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
		if RightFile==[]:
			prefix = f"{file_id} - " 					# finds a file based on its ID
			RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
			if RightFile==[]:
				prefix = "1-"
				RightFile = [filename for filename in os.listdir("history\\states") if filename.startswith(prefix)]
		print(RightFile)
		#print(RightFile==[])
		
		split3 = RightFile[0].split("- ")		# removes prefix from file name
		if not split3[1]:
			split3 = RightFile[0].split("-")
		else:
			print("noting to see here")
		FoundFile = split3[1].split(".")		# removes suffix from file name
		print(FoundFile[0])
		#if name != FoundFile[0]:				# checks of the stripped file name matches the new name, otherwise give errors
		#	if FoundFile[0] == 'txt':
		#		print(f"! The OG file didnt have a name (pushed file has name: {name})")
		#	if not name:
		#		print(f"! The new file has no name specified (pulled name was: {FoundFile[0]})")
		#	else:
		#		print(f"! The file pulled and pushed have different names ({FoundFile[0]} pulled, {name} pushed). You might want to double check the names")
		