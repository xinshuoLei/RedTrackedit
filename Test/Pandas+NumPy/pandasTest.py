import numpy
import pandas
import random

#Creating series (similar to arrays?)
s = pandas.Series([1, 3, 5, numpy.nan, 6, 8])
print(s)

#Creating Date Range
dates = pandas.date_range('20190602', '20190604',3)
print(dates)
numpyData = numpy.random.randn(3, 4)
for i in range(0, len(numpyData)):
	for j in range(0, len(numpyData[i])):
		print(numpyData[i][j], end=" ")
	print()
dataFrame = pandas.DataFrame(numpyData, index = dates, columns=list('ABCD'))
print(dataFrame)

#None is python's equivalent of null (HOWEVER, python CAN print None values)
variable = None
print(variable)

arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
dataFrame2 = pandas.DataFrame(arr, index = ["1-4","5-8", "9-12","13-16"], columns=["1*4", "2*4", "3*4", "4*4"])
print(dataFrame2)
#Print out dataframe index as index object
print(dataFrame2.index)
print(dataFrame.describe())

dataFrame.at['20190602', 'A'] = None
print(dataFrame)

dataFrame3 = dataFrame2.sort_values(by = "1*4", ascending = False)

print(dataFrame3)

randomArray = []
for i in range(0, 7):
	randomArray.append([])
	for j in range(0,50):
		randomArray[i].append(random.randint(0,25))

randomData = pandas.DataFrame(randomArray, index = ["A","B","C","D","E","F","G"]).T
randomData = randomData.sort_values(by = "A", ascending = True)
print(randomData)


sortData = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
        'age': [20, 19, 19, 21],
        'favorite_color': ['blue', 'red', 'yellow', "green"],
        'grade': [88, 92, 95, 70]}
dataFrame4 = pandas.DataFrame(sortData, index = sortData['name'])
print(dataFrame4)
dataFrame4 = dataFrame4.sort_values(by = ['age', 'grade'], ascending= [True, False])
print(dataFrame4)

data5 = {'Title': ['Article 1', 'Article 2' , 'Article 3', 'MEMEZ'], 'Upvotes': [5,104,104,38910], 'Downvotes': [0, 104, 1, 0], 'Comments': [2, 50, 23, 1045]}
dataFrame5 = pandas.DataFrame(data5, index = data5['Title'])
dataFrame5 = dataFrame5.sort_values(by = ['Upvotes', 'Downvotes'], ascending= [False, True])
print(dataFrame5)