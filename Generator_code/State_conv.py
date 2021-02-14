from csv import reader

with open('States_Raw.csv', 'r') as datalist:
	csv_reader = reader(datalist)
	for row in csv_reader:
#test