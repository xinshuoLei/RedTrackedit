import csv
import pandas
datafile = open('politics_top500.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')
pandas.set_option('display.max_columns', 8)
pandas.set_option('display.max_rows', 500)
data = []
for row in datareader:
	data.append(row)
lastData = []
for i in range(1,len(data)):
	lastData.append(data[i])
dataFrame = pandas.DataFrame(lastData, columns=data[0])
print(dataFrame)