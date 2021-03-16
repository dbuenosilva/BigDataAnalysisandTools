# -*- coding: utf-8 -*-
"""
Activities workshop 02
Date: 16/03/2021
Author: Diego Bueno da Silva
e-mail: d.bueno.da.silva.10@student.scu.edu.au
ID: 23567850
"""

import pandas as pd
import pathlib
path = pathlib.Path(__file__).resolve().parent
path = str(path) + "/datasets/"

""" Reading data from different files with different formats """

print("\nReading a CSV file with headers:")
myDataFrame = pd.read_csv( path + 'csv_mindex.csv')
print(myDataFrame)

print("\nReading a CSV file with headers by read_table function")
myDataFrame = pd.read_table( path + 'csv_mindex.csv',',')
print(myDataFrame)

print("\nReading a CSV file with headers renaming the colunms")
myDataFrame = pd.read_csv( path + 'ex2.csv',names = ['colunm A','colunm B','colunm C','colunm D'] )
print(myDataFrame)

print("\nReading a CSV file with headers by read_csv and indexing first colunm by number")
myDataFrame = pd.read_csv( path + 'stock_px_2.csv',index_col=1)
print(myDataFrame)

##myDataFrame = pd.read_csv( path + '/fec/P00000001-ALL.csv')
##print(myDataFrame)

print("\nReading a CSV file indexing multiple colunms")
print("Observed that index does not mean ordering, but it groups index contend hierarch")
##myDataFrame = pd.read_csv( path + '/fec/P00000001-ALL.csv',index_col=['cmte_id','cand_id'])
##print(myDataFrame)

print("\nReading a CSV file without delimitation")
myDataFrame = pd.read_table( path + 'ex3.txt')
print(myDataFrame)

print("\nReading a CSV file speficing by regex")
myDataFrame = pd.read_table( path + 'ex3.txt', sep="\s+")
print(myDataFrame)

print("\nReading file skipping some rows")
myDataFrame = pd.read_csv( path + 'ex2.csv')
print(myDataFrame)
print("\n--- skipping row 0")
myDataFrame = pd.read_csv( path + 'ex2.csv', skiprows=[0])
print(myDataFrame)

print("\nReading files with Null values and treating them:\n")
myDataFrame = pd.read_csv( path + 'ex5.csv')
print(myDataFrame)

print("\nReading files with Null values and showing them:\n")
myDataFrame = pd.read_csv( path + 'ex5.csv')
print(pd.isnull(myDataFrame))

print("\nReading files replacing values 'one' and 'foo' for NaN:\n")
## in all dataframe contend 'one' and 'foo' will be replaced by NaN
myDataFrame = pd.read_csv( path + 'ex5.csv', na_values=["one","foo"]) 
print(myDataFrame)

print("\nReading files replacing values for NaN using sentinels:\n")
## in each specific column contend will be replaced by NaN according to sentinels
sentinels = {"message": ['foo','world'], "b":[2,0], "c":[3,0], "d":[4,0]}
myDataFrame = pd.read_csv( path + 'ex5.csv', na_values=sentinels)
print(myDataFrame)

def myUpper(parameter = "") :
    return(parameter.upper())

print("\nReading files replacing values according to function:\n")
MyConverter = { "message" : myUpper }
myDataFrame = pd.read_csv( path + 'ex5.csv', converters=MyConverter )
print(myDataFrame)

print("\nDefining number of rows to read:\n")
myDataFrame = pd.read_csv( path + '/fec/P00000001-ALL.csv',nrows = 10)
print(myDataFrame)
 
print("pd.options.display.max_rows can be set")
print("pd.options.display.max_rows: ", pd.options.display.max_rows)
print("\nDefining number of rows to read:\n")
myDataFrame = pd.read_csv( path + '/fec/P00000001-ALL.csv',nrows = 10)
print(myDataFrame)



""" 	Reading Text Files in Pieces """


print("\nSplitting the file into chunck and print 10th piece:\n")
myDataFrameChuncker = pd.read_csv( path + '/fec/P00000001-ALL.csv',chunksize = 10000)

i = 0
# print only the last piece
for piece in myDataFrameChuncker:
    i+=1
    if i == 10 :
        print(piece["cand_id"])
        

"""  Writing Data to Text Format """

print("\nReading a CSV file and writing to Execel format")
myDataFrame = pd.read_csv( path + 'ex2.csv', names = ['id','colunm A','colunm B','colunm C','colunm D'])
print(myDataFrame)
print("\nWriting to MS Excel")
#myDataFrame.to_excel( path + 'ex2Out.xlsx' )
#print(myDataFrame)

print("\nReading a XLS file and writing to CSV format")
myDataFrame = pd.read_excel( path + 'ex2Out.xlsx')
print(myDataFrame)
print("\nWriting to CSV")
myDataFrame.to_csv( path + 'ex2Out.csv' )
print(myDataFrame)

import sys

print("\nPrinting to CSV result with special delimiter")
print(myDataFrame.to_csv(sys.stdout, sep = '|' ) )

myDataFrame = pd.read_csv( path + 'ex5.csv') 
print("\nPrinting to CSV result with special NaN")
print(myDataFrame.to_csv(sys.stdout, na_rep = 'NULL' ) )


print("\nDisabling rows and columns names:")
print(myDataFrame.to_csv(sys.stdout, index=False, header=False ) )


print("\nPrinting only colunms something and message:")
print(myDataFrame.to_csv(sys.stdout, na_rep = 'NULL', index=False, columns=["something","message"] ) )


"""  Working with Delimited Formats 


"a","b","c"
"1","2","3"
"1","2","3"

"""
import csv

myFile = open( path + 'ex7.csv')

myCsv = csv.reader(myFile, delimiter=',')

# csv object needs to be iterated
for line in myCsv:
    print(line) 

print("\nEach line looks a array, let's see line[0]")
print(line[0])

print("\nCreating a dictonary from the CSV object")

###AllLines = list(myCsv) I did not understand why it is not working
with open( path +  'ex7.csv') as f:
    AllLines = list(csv.reader(f))

myHeader, myRows = AllLines[0], AllLines[1:]

print("AllLines", AllLines)
print("myHeader:", myHeader)
print("myRows: ", myRows)


myDict = {h: v for h, v in zip(myHeader, zip(*myRows))}
print(myDict)

print("\nPersonalising CSVs dialect")

class my_dialect(csv.Dialect):
    lineterminator = '\n' 
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_NONE

myCsvByDialect = csv.reader(myFile, dialect=my_dialect)
for line in myCsvByDialect:
    print(line) ## did not print



print("\nWriting a CSV file")

with open( path + 'myFile.csv', 'w') as f_output:
    writer = csv.writer(f_output, dialect=my_dialect)
    writer.writerow(('product', 'qtd', 'total' ))
    writer.writerow(('apple', '12', 3 ))
    writer.writerow(('banana', '6', 1.5 ))
    writer.writerow(('orange', '25', 12.5 ))
    
myCsv = csv.reader(open( path + 'myFile.csv'))
    
for line in myCsv:
    print(line) 
    
    
"""  Working with JSON data """

print("\nCreating and converting to JSON obj") 

MyJsonString = """
    {"name": "Diego",
    "places_lived": ["Jungle", "Brasilia", "Australia"],
    "pet": null,
    "siblings": [{"name": "Diogenes", "age": 41, "pets": null},
                  {"name": "Laila", "age": 39,"pets": ["Rex", "Lesse"]},
                  {"name": "Norram", "age": 36,"kids": ["Murilo", "Miguel"]}]
    } 
    """

import json

MyJsonObj = json.loads(MyJsonString)

print(MyJsonObj)

print("\nConverting from JSON to string")
dumppedJson = json.dumps(MyJsonObj)
print(type(dumppedJson))


print("\nConverting JSON Obj to DataFrame")
mySiblings = pd.DataFrame(MyJsonObj['siblings'], columns=['name','age'])

print("\nmySiblings:\n", mySiblings)

MyJsonString = """
    [{"name": "Diogenes", "age": 41, "pets": null},
    {"name": "Laila", "age": 39,"pets": ["Rex", "Lesse"]},
    {"name": "Norram", "age": 36,"kids": ["Murilo", "Miguel"]
    }] 
    """
    
print("\nConverting JSON files to DataFrame")
jsonFile = open(path + "myJson.json", "w") # append
jsonFile.write(MyJsonString)
jsonFile.close()

myDataFrame = pd.read_json( path + "myJson.json" )

print(myDataFrame) # it does not work well when Json is deeper



""" XML and HTML: Web Scraping """

#conda install lxml
#pip install beautifulsoup4 html5lib










