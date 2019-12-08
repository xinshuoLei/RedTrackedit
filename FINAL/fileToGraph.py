import os
from CSVtoSortedDataFrame import *
from graphingMain import *
import pandas_bokeh

def scatter(toGraph):
    for root, dirs, files in os.walk(".", topdown=False):
       for filename in files:
           if filename == toGraph:
               dataFrame = getPandasDataFrame(filename)
               return plot_scatter(dataFrame,filename)
if __name__ == "__main__":
    scatter(input("Enter name: "))
