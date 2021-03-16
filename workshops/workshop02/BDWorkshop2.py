#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data Loading, Storage, and File Formats: Chapter 6


# In[2]:


import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt


# ## Reading and Writing Data in Text Format

# In[3]:


# Reading a small comma-separated (CSV) text file
path = 'C:/Users/aalaei/OneDrive - Southern Cross University/MyLapTop/SCU/MIT_Big_Data_Analysis_and_Tools/Designed Unit-S2-2020/Workshops/Examples_Book_Python for data analysis/'
fname1=path+'ex1.csv'
df = pd.read_csv(fname1)
df


# In[4]:


# use read_table and specified the delimiter
pd.read_table(fname1, sep=',')


# In[5]:


# Reading a comma-separated (CSV) file having no column names
# You can allow pandas to assign default column names
fname2=path+'ex2.csv'
pd.read_csv(fname2, header=None)


# In[5]:


# you can specify names of the columns yourself
fname2=path+'ex2.csv'
pd.read_csv(fname2, names=['aa', 'bb', 'cc', 'dd', 'message'])


# In[6]:


# the message column to be the index of the returned DataFrame.
names1 = ['a', 'b', 'c', 'd', 'message']
pd.read_csv(fname2, names=names1, index_col='message')


# In[7]:


# you want to form a hierarchical index from multiple columns, pass a
# list of column numbers or names
fname3=path+'csv_mindex.csv'
parsed = pd.read_csv(fname3,index_col=['key1', 'key2'])
parsed


# In[8]:


fname4=path+'ex3.txt'
list(open(fname4))


# In[9]:


# Missing data is usually either not present (empty string) or marked by
# some sentinel value. By default, pandas uses a set of commonly occurring sentinels,
# such as NA and NULL
fname5=path+'ex5.csv'
result = pd.read_table(fname5, sep=',')
result


# In[16]:


pd.isnull(result)


# In[18]:


# The na_values option can take either a list or set of strings to 
# consider missing values
result = pd.read_csv(fname5, na_values=['NULL'])
result


# In[15]:


# Different NA sentinels can be specified for each column in a dict:
sentinels = {'message': ['foo', 'NA'], 'something': ['three',]}
pd.read_csv(fname5, na_values=sentinels)


# # Reading Text Files in Pieces
# When processing very large files or figuring out the right set of arguments to correctly process a large file, you may only want to read in a small piece of a file or iterate through smaller chunks of the file. 

# In[20]:


# we make the pandas display settings more compact showing only 10 rows
pd.options.display.max_rows = 10


# In[16]:


fname6=path+'ex6.csv'
result = pd.read_csv(fname6)
result


# In[17]:


# If you want to only read a small number of rows (avoiding reading the entire file),
# specify that with nrows
df=pd.read_csv(fname6, nrows=5)
df


# In[18]:


# To read a file in pieces, specify a chunksize as a number of rows
chunker = pd.read_csv(fname6, chunksize=1000)
chunker


# In[28]:


# The TextParser object returned by read_csv allows you to iterate over the parts of
#the file according to the chunksize. 
#For example, we can iterate over ex6.csv, aggregating the value counts in the 'key' column
chunker = pd.read_csv(fname6, chunksize=1000)

tot = pd.Series([], dtype="float")
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)


# In[35]:


print(tot[:10], sum(tot))


# ### Writing Data to Text Format

# In[20]:


mydata = pd.read_csv(fname5)
mydata


# In[22]:


# Using DataFrame’s to_csv method, we can write the data out to a csv file
fnameo=path+'out.csv'
mydata.to_csv(fnameo)
#!type fnameo


# In[23]:


# Other delimiters can be used
# writing to sys.stdout so it prints the text result to the console
import sys
mydata.to_csv(sys.stdout, sep='|')


# In[27]:


# Missing values appear as empty strings in the output. 
# You might want to denote them by some other sentinel value:
mydata.to_csv(sys.stdout, na_rep='NULL')


# In[28]:


# With no other options specified, both the row and column labels are written. 
# Both of these can be disabled:
mydata.to_csv(sys.stdout, index=False, header=False)


# In[29]:


# You can write only a subset of the columns, and in an order of your choice!
mydata.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])


# In[36]:


# Series also has a to_csv method:
fname7=path+'tseries.csv'
dates = pd.date_range('1/1/2000', periods=35)
ts = pd.Series(np.arange(35), index=dates)
ts.to_csv(fname7)
ts


# ### Working with Delimited Formats

# In[37]:


# "a","b","c"
# "1","2","3"
# "1","2","3"
# For any file with a single-character delimiter, you can use Python’s built-in csv module.
# To use it, pass any open file or file-like object to csv.reader

import csv
fname8=path+'ex7.csv'
f = open(fname8)

reader = csv.reader(f)


# In[38]:


# Iterating through the reader like a file yields tuples of values 
# with any quote characters removed
for line in reader:
    print(line)


# In[40]:


# From there, you can do the wrangling necessary to put the data in the form
# that you need it. To do so, first, read the file into a list of lines:
with open(fname8) as f:
    lines = list(csv.reader(f))
lines


# In[42]:


# Then, split the lines into the header line and the data lines:
header, values = lines[0], lines[1:]


# In[43]:


# Then we can create a dictionary of data columns using a dictionary comprehension
# and the expression zip(*values), which transposes rows to columns
data_dict = {h: v for h, v in zip(header, zip(*values))}
data_dict


# class my_dialect(csv.Dialect):
#     lineterminator = '\n'
#     delimiter = ';'
#     quotechar = '"'
#     quoting = csv.QUOTE_MINIMAL
# reader = csv.reader(f, dialect=my_dialect)

# reader = csv.reader(f, delimiter='|')

# with open('mydata.csv', 'w') as f:
#     writer = csv.writer(f, dialect=my_dialect)
#     writer.writerow(('one', 'two', 'three'))
#     writer.writerow(('1', '2', '3'))
#     writer.writerow(('4', '5', '6'))
#     writer.writerow(('7', '8', '9'))

# ### JSON Data

# In[44]:


# JSON (short for JavaScript Object Notation) has become one of the standard formats
# for sending data by HTTP request between web browsers and other applications. 
# It is a much more free-form data format than a tabular text form like CSV.
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""


# In[45]:


# To convert a JSON string to Python form, use json.loads:
import json
result = json.loads(obj)
result


# In[3]:


# json.dumps converts a Python object back to JSON:
asjson = json.dumps(result)


# In[47]:


# How you convert a JSON object or list of objects to a DataFrame or some other data structure for analysis
# Conveniently, you can pass a list of dicts the DataFrame constructor and select a subset of the data fields
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age', 'pets'])
siblings


# In[8]:


# The pandas.read_json can automatically convert JSON datasets in specific arrangements
# into a Series or DataFrame
# The default options for pandas.read_json assume that each object in the JSON array
# is a row in the table:
fname9=path+'example.json'
data = pd.read_json(fname9)
data


# In[9]:


# If you need to export data from pandas to JSON, one way is to use the to_json methods on Series and DataFrame
print(data.to_json())
print(data.to_json(orient='records'))


# ### XML and HTML: Web Scraping

# conda install lxml
# pip install beautifulsoup4 html5lib

# In[48]:


# Python has many libraries for reading and writing data in the ubiquitous HTML and XML formats.
# pandas has a built-in function, read_html, which uses libraries like lxml and Beautiful
# Soup to automatically parse tables out of HTML files as DataFrame objects.
fname10=path+'fdic_failed_bank_list.html'
tables = pd.read_html(fname10)
print(len(tables))
failures = tables[0]
failures.head()


# In[49]:


# we can proceed to do some data cleaning and analysis, like computing the number of bank failures by year
update_timestamps = pd.to_datetime(failures['Updated Date'])
update_timestamps.dt.year.value_counts()


# #### Parsing XML with lxml.objectify

# In[15]:


# XML (eXtensible Markup Language) is another common structured data format supporting hierarchical,
# nested data with metadata.
    <INDICATOR>
        <INDICATOR_SEQ>373889</INDICATOR_SEQ>
        <PARENT_SEQ></PARENT_SEQ>
        <AGENCY_NAME>Metro-North Railroad</AGENCY_NAME>
        <INDICATOR_NAME>Escalator Availability</INDICATOR_NAME>
        <DESCRIPTION>Percent of the time that escalators are operational
        systemwide. The availability rate is based on physical observations performed
        the morning of regular business days only. This is a new indicator the agency
        began reporting in 2009.</DESCRIPTION>
        <PERIOD_YEAR>2011</PERIOD_YEAR>
        <PERIOD_MONTH>12</PERIOD_MONTH>
        <CATEGORY>Service Indicators</CATEGORY>
        <FREQUENCY>M</FREQUENCY>
        <DESIRED_CHANGE>U</DESIRED_CHANGE>
        <INDICATOR_UNIT>%</INDICATOR_UNIT>
        <DECIMAL_PLACES>1</DECIMAL_PLACES>
        <YTD_TARGET>97.00</YTD_TARGET>
        <YTD_ACTUAL></YTD_ACTUAL>
        <MONTHLY_TARGET>97.00</MONTHLY_TARGET>
        <MONTHLY_ACTUAL></MONTHLY_ACTUAL>
    </INDICATOR>


# In[50]:


# Using lxml.objectify, we parse the file and get a reference to the root node of the XML file with getroot:

from lxml import objectify

fname12='C:/Users/aalaei/OneDrive - Southern Cross University/MyLapTop/SCU/MIT_Big_Data_Analysis_and_Tools/Designed Unit-S2-2020/Workshops/Datasets_Book_Python for data analysis/mta_perf/Performance_MNR.xml'

parsed = objectify.parse(open(fname12))
root = parsed.getroot()


# In[51]:


# For each record, we can populate a dict of tag names (like YTD_ACTUAL) to data values 

data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)


# In[26]:


# Lastly, convert this list of dicts into a DataFrame:
perf = pd.DataFrame(data)
perf.head()


# In[52]:


# XML data can get much more complicated than this example. Each tag can have
# metadata, too. Consider an HTML link tag, which is also valid XML:
from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()


# In[53]:


# You can now access any of the fields (like href) in the tag or the link text:
root
print(root.get('href'))
print(root.text)


# ## Binary Data Formats

# In[54]:


# One of the easiest ways to store data (also known as serialization) efficiently in binary
# format is using Python’s built-in pickle serialization. pandas objects all have a
# to_pickle method that writes the data to disk in pickle format

frame = pd.read_csv(fname1)
print(frame)
fname13=path+'frame_pickle'
frame.to_pickle(fname13)


# In[55]:


# You can read any “pickled” object stored in a file by using the built-in pickle directly,
# or even more conveniently using pandas.read_pickle:
pd.read_pickle(fname13)


# 
# ### Using HDF5 Format

# In[56]:


# HDF: hierarchical data format.
# HDF5 is a well-regarded file format intended for storing large quantities of scientific array data.
# The HDFStore class works like a dict and handles the low-level details:
frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
store


# In[57]:


store['obj1']


# In[59]:


# HDFStore supports two storage schemas, 'fixed' and 'table'. The latter is generally
# slower, but it supports query operations using a special syntax
# The put is an explicit version of the store['obj2'] = frame method but allows us to
# set other options like the storage format.
store.put('obj2', frame, format='table')
store.select('obj2', where=['index >= 10 and index <= 15'])
store.close()


# In[60]:


# The pandas.read_hdf function gives you a shortcut to these tools:
frame.to_hdf('mydata.h5', 'obj3', format='table')
pd.read_hdf('mydata.h5', 'obj3', where=['index < 5'])


# In[41]:


import os
os.remove('mydata.h5')


# ### Reading Microsoft Excel Files

# In[62]:


# Pandas supports reading tabular data stored in Excel 2003 (and higher) files
# using either the ExcelFile class or pandas.read_excel function.
fname14=path+'ex1.xlsx'
xlsx = pd.ExcelFile(fname14)


# In[63]:


# Data stored in a sheet can then be read into DataFrame with parse:
pd.read_excel(xlsx, 'Sheet1')


# In[44]:


# If you are reading multiple sheets in a file, then it is faster to create the ExcelFile,
# you can also simply pass the filename to pandas.read_excel
frame = pd.read_excel(fname14, 'Sheet1')
frame


# In[45]:


# To write pandas data to Excel format, you must first create an ExcelWriter, then
# write data to it using pandas objects’ to_excel method
fname15=path+'ex2.xlsx'
writer = pd.ExcelWriter(fname15)
frame.to_excel(writer, 'Sheet1')
writer.save()


# In[ ]:


#You can also pass a file path to to_excel and avoid the ExcelWriter
frame.to_excel(fname15)


# ## Interacting with Web APIs

# In[64]:


# Many websites have public APIs providing data feeds via JSON or some other format.
# There are a number of ways to access these APIs from Python
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp


# In[65]:


# The Response object’s json method will return a dictionary containing JSON parsed
# into native Python objects
data = resp.json()
data[0]['title']
data


# In[66]:


# Each element in data is a dictionary containing all of the data found on a GitHub
# issue page (except for the comments). We can pass data directly to DataFrame and
# extract fields of interest
issues = pd.DataFrame(data, columns=['id', 'user', 'number', 'title',
                                     'labels', 'state'])
issues


# ## Interacting with Databases

# In[68]:


# Loading data from SQL into a DataFrame is fairly straightforward, and pandas has
# some functions to simplify the process. As an example, a SQLite database is created
# using Python’s built-in sqlite3 driver
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""
con = sqlite3.connect('mydata1.sqlite')
con.execute(query)
con.commit()


# In[69]:


# Insert a few rows of data:
data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()


# In[70]:


# Most Python SQL drivers (PyODBC, psycopg2, MySQLdb, pymssql, etc.) return a list
# of tuples when selecting data from a table
cursor = con.execute('select * from test')
rows = cursor.fetchall()
rows


# In[58]:


# You can pass the list of tuples to the DataFrame constructor, but you also need the
# column names, contained in the cursor’s description attribute
print(cursor.description)
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])


# In[71]:


# The SQLAlchemy project is a popular Python SQL toolkit that abstracts
# away many of the common differences between SQL databases. pandas has a
# read_sql function that enables you to read data easily from a general SQLAlchemy
# connection. Here, we’ll connect to the same SQLite database with SQLAlchemy and
# read data from the table created before
import sqlalchemy as sqla
db = sqla.create_engine('sqlite:///mydata1.sqlite')
pd.read_sql('select * from test', db)


# ## Conclusion
