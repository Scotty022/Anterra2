# Set limit on what range to generate
LimitL = 1
LimitU = 1000

from csv import reader
import os
import sys

Output = 'Generator_code\\Output\\'
Source = 'history\\countries\\'

print("The script has started. Please do not touch any files")

List = [filename for filename in os.listdir(Source)]

for Country in List:
	ID = Country.split(" - ",1)[0]
	print(ID)

	try:
		g = open(ID+".txt")


