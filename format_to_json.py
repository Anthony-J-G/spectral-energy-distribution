import json
import csv
from os import listdir

path = "data\\"

files = listdir(path + 'raw\\') # lists all the file names in the 'path' directory
num_files = len(files) # stores the number of files in the 'path' directory

def return_csv(file):
	csv_dict = {}
	with open(file) as csv_file:
		csv_read = csv.reader(csv_file)

		i = 0
		for line in csv_read:
			if i == 0:
				# Initialize csv dictionary with header values as keys
				for key in line:
					csv_dict[key] = []
				i += 1
				continue
			
			# Add the value in the csv to the corresponding key
			index = 0
			for key in csv_dict:
				csv_dict[key].append(line[index])
				index+=1
			i +=1

	return csv_dict


data = {}

for file in files:
	name = file.replace('_Photometry_and_SED.csv', '')
	print(name)
	data[name] = return_csv(path + 'raw\\' + file)


with open(path + 'formatted_data.json', 'w') as f:
	json.dump(data, f, indent=2)




