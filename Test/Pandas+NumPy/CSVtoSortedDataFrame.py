import csv
import pandas

#dataPath is the file which is being imported to be turned into dataframe in the format: exampleFile.csv
def importCSV(dataPath):
	datafile = open(dataPath, 'r')
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
	dataFrame.score = pandas.to_numeric(dataFrame.score)
	dataFrame.comms_num = pandas.to_numeric(dataFrame.comms_num)
	return dataFrame

def sortDataFrame(dataFrame):
	dataFrame = dataFrame.sort_values(by = ['score', 'comms_num', 'created'], ascending = [False, False, True])
	return dataFrame

def getPandasDataFrame(dataPath):
	return sortDataFrame(importCSV(dataPath))

print(getPandasDataFrame('politics_top500.csv'))
