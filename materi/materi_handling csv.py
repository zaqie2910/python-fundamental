import csv

print('--- IMPORT DATA JAJAN ---')
with open('jajan.csv', 'r', newline='') as file:
	reader = csv.reader(file)
	header = next(reader)
	print(header)
	for row in reader:
		print(row)
