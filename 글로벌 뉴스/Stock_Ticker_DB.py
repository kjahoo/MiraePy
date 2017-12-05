import csv
nyse = []

f = open('NYSE_20171204.txt','r')
csvReader = csv.reader(f)

for row in csvReader:
    nyse.append(row)

print(nyse)

f.close()
