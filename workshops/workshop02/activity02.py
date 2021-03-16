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
dfMindex = pd.read_csv( path + 'csv_mindex.csv')
print(dfMindex)

print("\nReading a CSV file with headers by read_table function")
dfMindex = pd.read_table( path + 'csv_mindex.csv',',')
print(dfMindex)

print("\nReading a CSV file with headers renaming the colunms")
dfMindex = pd.read_csv( path + 'ex2.csv',names = ['colunm A','colunm B','colunm C','colunm D'] )
print(dfMindex)

print("\nReading a CSV file with headers by read_csv and indexing first colunm by number")
dfMindex = pd.read_csv( path + 'stock_px_2.csv',index_col=1)
print(dfMindex)

##dfMindex = pd.read_csv( path + '/fec/P00000001-ALL.csv')
##print(dfMindex)

print("\nReading a CSV file indexing multiple colunms")
print("Observed that index does not mean ordering, but it groups index contend hierarch")
##dfMindex = pd.read_csv( path + '/fec/P00000001-ALL.csv',index_col=['cmte_id','cand_id'])
##print(dfMindex)

print("\nReading a CSV file without delimitation")
dfMindex = pd.read_table( path + 'ex3.txt')
print(dfMindex)

print("\nReading a CSV file speficing by regex")
dfMindex = pd.read_table( path + 'ex3.txt', sep="\s+")
print(dfMindex)

print("\nReading file skipping some rows")
dfMindex = pd.read_csv( path + 'ex2.csv')
print(dfMindex)
print("\n--- skipping row 0")
dfMindex = pd.read_csv( path + 'ex2.csv', skiprows=[0])
print(dfMindex)

print("\nReading files with Null values and treating them:\n")
dfMindex = pd.read_csv( path + 'ex5.csv')
print(dfMindex)

print("\nReading files with Null values and showing them:\n")
dfMindex = pd.read_csv( path + 'ex5.csv')
print(pd.isnull(dfMindex))
















