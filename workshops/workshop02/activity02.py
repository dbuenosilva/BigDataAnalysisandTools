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

myDataFrame = pd.read_csv( path + '/fec/P00000001-ALL.csv')
print(myDataFrame)

print("\nReading a CSV file indexing multiple colunms")
print("Observed that index does not mean ordering, but it groups index contend hierarch")
myDataFrame = pd.read_csv( path + '/fec/P00000001-ALL.csv',index_col=['cmte_id','cand_id'])#print(myDataFrame)

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

print("\nReading a HTML file with pandas")
tablesDfFromHTML = pd.read_html( path + "fdic_failed_bank_list.html" )

if len(tablesDfFromHTML) > 0:
    print("\nLoaded ", len(tablesDfFromHTML), " table(s) from fdic_failed_bank_list.html file.\n")

    print(tablesDfFromHTML[0].head())

    close_data = pd.to_datetime(tablesDfFromHTML[0]['Closing Date'])

    print("\nQuantity of closed banks per year:\nit looks that 2008 GFC provoked a huge problem in 2009 and 2010...\n")
    print(close_data.dt.year.value_counts())


print("\nParsing a XML file with lxml.objectify\n")

from lxml import objectify 
parsedXML = objectify.parse(open(path + "mta_perf/Performance_LIBUS.xml"))
root =  parsedXML.getroot()

myData = []
skip_fields = ['PARENT_SEQ','INDICATOR_SEQ','DESIRED_CHANGE','DECIMAL_PLACES']

for elt in root.INDICATOR: 
    el_data = {}
    for child in elt.getchildren(): 
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval 
    myData.append(el_data)
    

myDataFrame = pd.DataFrame(myData)

print(myDataFrame.head())


tag = '<a href="http://www.gwaya.com">Gwaya</a>'
print("\nParsing ", tag," HTML contend with lxml.objectify")
from io import StringIO

root = objectify.parse(StringIO(tag)).getroot()

print("\nroot.get('href'): ", root.get('href'))
print("root.text: ", root.text)

""" Binary Data Formats """

print("Writing a pickle serialization")

myDataFrame = pd.read_csv( path + 'csv_mindex.csv')
print(myDataFrame)

myDataFrame.to_pickle( path + 'pickle_mindex' )

print("\nThe pickle file became 10x larger than csv :(\n" )
print(pd.read_pickle( path + 'pickle_mindex' ))



""" Using HDF5 Format """ 
##  pip install tables

print("\nInputting the dataframe 'myDataFrame' to HDF5 file  \n" )

# Create the file
myStoreHDF5 = pd.HDFStore(path + 'myData.h5')

myStoreHDF5.put('myDataFrame', myDataFrame, format='table')

print("\nRetrieving contend from myStoreHDF5 file")
print(myStoreHDF5.select('myDataFrame'))

print("\nInputting the pickle file 'pickle_mindex' to HDF5 store  \n" )
myStoreHDF5.put('pickle_mindex', pd.read_pickle( path + 'pickle_mindex' ), format='table')

print("\nRetrieving pickle_mindex contend from myStoreHDF5 store")
print(myStoreHDF5.select('pickle_mindex'))



""" Reading Microsoft Excel Files 

print("\nReading specific spreadsheet of Excel file\n")
myDataFrame = pd.read_excel( path + 'ex2.xlsx', 'Sheet1')

print(myDataFrame)


print("\nInputting a new sheet in spreadsheet of Excel file\n")
writer = pd.ExcelWriter(path + 'ex2.xlsx')
myDataFrame.to_excel(writer, 'Copy of Sheet1 by Python')
writer.save()

print(pd.read_excel( path + 'ex2.xlsx', 'Copy of Sheet1 by Python'))

print("\nOPS! It replaced sheet1... ValueError: Append mode is not supported with xlsxwriter!")                                                                


""" 


""" Interacting with Web APIs """ 


import requests
print("\nRetriaving JSON from Web HTTP methods\n")

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)

result = resp.json()

print("It returned objet type ",type(result)) 

print("\nConverting retrieved JSON to DataFrame")
print(pd.DataFrame(result, columns=['number','title','labels','state']))




""" Interacting with Relational Databases """

import sqlite3

print("\nCreating sqllite database\n")
con = sqlite3.connect( path + 'mydata.sqlite')

query = "drop table sales;"
con.execute(query)

query = """
create table sales
(product VARCHAR(20), qtd INTEGER, total REAL)
;"""
con.execute(query)
con.commit()

print("\nInserting myFile.csv into sqllite database\n")
myCsv = csv.reader(open( path + 'myFile.csv'))

aDados = []
header = 0
for line in myCsv:
    if header > 0:
        aDados.append((tuple(line)))
    header+=1

query = "insert into sales values (?, ?, ?) "
con.executemany(query, aDados)
con.commit()

print("\nRetrieving sqllite data with sqlalchemy\n")

#sqlalchemy
import sqlalchemy as sqla
db = sqla.create_engine('sqlite:///'+ path + 'mydata.sqlite')
print(pd.read_sql('select * from sales', db))





 