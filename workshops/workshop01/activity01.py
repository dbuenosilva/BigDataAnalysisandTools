# -*- coding: utf-8 -*-
"""
Activities workshop 01
Date: 05/03/2021
Author: Diego Bueno da Silva
e-mail: d.bueno.da.silva.10@student.scu.edu.au
ID: 23567850
"""

""" Tuples """

## Tuples
simpleTuple = 0, 1
boolSimpleTuple = True, False
anyValuesTuple = None, 0, 'a'
nestedTupleSample = (0,1), (True, False), (None, 0, 'a')

## Converting list to tuple
simpleList = [0,4,10]
convertedListToTuple = tuple(simpleList)

## Converting string to tuple
simpleString = 'I loved doing it in C'
simpleStringIntoTuple = tuple(simpleString)
print(simpleStringIntoTuple)

## Accessing elements
print("First element: ",simpleStringIntoTuple[0])
print("Last element: ",simpleStringIntoTuple[len(simpleStringIntoTuple)-1])

## Only all tuple can be replaced
simpleStringIntoTuple = tuple('New contend!')
print(simpleStringIntoTuple)
#simpleStringIntoTuple[0] = tuple('E!') ## TypeError: 'tuple' object does not support item assignment

# however, if list you may append
tupleOfLists = tuple([ [0,0,0] ,2,4 ])
tupleOfLists[0].append(6)
print(tupleOfLists)

# concatenating tuples (bit weird)
concatedTuple = tupleOfLists + simpleStringIntoTuple
print(concatedTuple)

# mult concatenating
## The objects themselves are not copied, only the references to them :)
print(simpleTuple * 4)

# unpacking tuples ( very useful! )
binarios, booleanos, mix = nestedTupleSample
a, b = binarios
opc1, opc2 = booleanos
result, number, character = mix

# swapping variables :)
print("opc1",opc1)
print("opc2",opc2)
print("swapping...")

opc1, opc2 = opc2, opc1 

print("opc1",opc1)
print("opc2",opc2)

seq=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))

# unwanted variables ( _ by convention )
binarios, *_ = nestedTupleSample

# counting elements. It should be a tuple as parameter
print( seq.count( (1,2,3) )   )

""" Operating with lists  """

# casting to a list
aListExample = list(seq)
print(aListExample) # list of tuples.
aDeepList = list(aListExample[0])
aDeepList[0] = 0
print(aDeepList)

# casting range to list
rangeOfTen = range(10)
print("rangeOfTen: ", rangeOfTen)
listOfTen = list(rangeOfTen)
print("listOfTen: ", listOfTen)

# appending
listOfTen.append(10)
print("listOfTen got 11 elements: ", listOfTen)

# inserting into a specific position
listOfTen.insert(5,'weird no integer element in the list')
print("listOfTen got 12 elements: ", listOfTen)

# removing elements
if 'weird no integer element in the list' in listOfTen:
    listOfTen.remove('weird no integer element in the list')

listOfTen.pop(10)

print("listOfTen got back 10 elements: ", listOfTen )

# concatenating list
newList = listOfTen + aListExample
print("newList: ", newList)

# extend is faster and better performance than simple concatenating
newList.extend(["extending the list", False, None, 4.5])
print("extended newList: ", newList)

# sorting
listOfTen.sort()
print("listOfTen sorted: ", listOfTen)

# binary search and insert
import bisect

# finding the position
position = bisect.bisect(listOfTen, 5.5)
print(position)

bisect.insort(listOfTen, 5.5)
print("listOfTen sorted with 5.5 included: ", listOfTen)

# Slicing
print("newList[10:] ", newList[10:])
print("newList[10:10] ", newList[10:11])
print("newList[:10] ", newList[:10])

newList[10:14] = [10,11,12,13] # loco
print("newList ", newList)

# negative indices
print(newList[-5:-1])

print("newList[:5] ( 0 to 5 ) ", newList[:5])

# Finally, I undertood what :: does :)
print("newList[::5] ( step plus 5 ) ", newList[::5])

print("listOfTen reversed: ", listOfTen[::-1])

























