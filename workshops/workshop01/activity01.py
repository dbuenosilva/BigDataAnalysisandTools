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




