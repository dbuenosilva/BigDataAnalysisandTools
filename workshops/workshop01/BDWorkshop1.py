#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Data Structures and Sequences: Tuple, List, Dict, Set
# Important Data Structures and Sequences in Python
# Tuple: is a fixed-length, immutable sequence of Python objects
# easiest way to create one is with a comma-separated sequence of values
tup = 4, 5, 6
tup


# In[3]:


nested_tup = (4, 5, 6), (7, 8)
nested_tup


# In[7]:


nested_tup = (4, 5, 6), (7, 8), tuple([4, 0, 2])
nested_tup


# In[4]:


tups = tuple('string')
tups [1]


# In[5]:


tup = tup,tups 
tup


# In[6]:


tup = tup,tups 
print (tup)
tup[1][0]


# In[15]:


tupm = tuple(['foo', [1, 2], True])
tupm


# In[38]:


tupm[2]


# In[16]:


tupm[2] = False


# In[17]:


tupm[1].append(3)
tupm


# In[12]:


tupm = tupm + (4, None, 'foo') + (6, 0) + ('bar',)
tupm


# In[18]:


tupm =tupm + ('foo', 'bar') * 4
tupm


# In[19]:


# Unpacking tuples
tup = (4, 5, 6)
a, b, c = tup
b


# In[21]:


# Unpacking nested tuples
tup = 4, 5, (6, 7)
print(tup)
a, b, (c, d) = tup
d


# In[22]:


# swapping values of two variables
a, b = 1, 2
print(a,b)
b, a = a, b
print(a,b)


# In[23]:


#A common use of variable unpacking is iterating over sequences of tuples or lists:
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))


# In[24]:


# This uses the special syntax *rest, which is also used in function signatures
# to capture an arbitrarily long list of positional arguments:
values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a,b, rest)


# In[25]:


# the underscore (_) for unwanted variables
a, b, *_ = values
print(a,b, _)


# In[27]:


# counts the number of occurrences of a value
a = (1, 2, 2, 2, 3, 4, 2)
a.count(3)


# In[28]:


# In contrast with tuples, lists are variable-length and their contents can be modified
# in-place. You can define them using square brackets []
a_list = [2, 3, 7, None]
a_list


# In[29]:


tup = ('foo', 'bar', 'baz')
tup


# In[30]:


b_list = list(tup)
b_list


# In[31]:


b_list[1] = 'peekaboo'
b_list


# In[32]:


gen = range(10)
gen
list(gen)


# In[33]:


b_list.append('dwarf')
b_list


# In[34]:


b_list.insert(1, 'red')
b_list


# In[35]:


ril=b_list.pop(2)
print(ril)
print(b_list)


# In[36]:


b_list.append('foo')
b_list


# In[37]:


b_list.remove('foo')
b_list


# In[38]:


'dwarf' in b_list


# In[72]:


'dwarf' not in b_list


# In[73]:


[4, None, 'foo'] + [7, 8, (2, 3)]


# In[39]:


x = [4, None, 'foo']


# In[40]:


x.extend([7, 8, (2, 3)])
x


# In[42]:


x[5][1]


# In[43]:


a = [7, 2, 5, 1, 3]
a.sort()
a


# In[44]:


b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
b


# In[45]:


import bisect
c = [1, 2, 2, 2, 3, 4, 7]
bisect.bisect(c, 2)


# In[46]:


bisect.bisect(c, 5)


# In[85]:


bisect.insort(c, 6)
c


# In[47]:


seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]


# In[48]:


seq[3:4] = [8, 8, 8]
seq


# In[49]:


seq[:5]


# In[96]:


seq[3:]


# In[50]:


seq[-4:]


# In[98]:


seq[-6:-2]


# In[99]:


seq[::2]


# In[100]:


seq[::-1]


# In[52]:


some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
mapping


# In[55]:


mapping['foo']


# In[56]:


sorted([7, 1, 2, 6, 0, 3, 2])


# In[57]:


sorted('horse race')


# In[58]:


seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
list(zipped)


# In[59]:


seq3 = [False, True]
seq4=list(zip(seq1, seq2, seq3))
seq4


# In[60]:


for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))


# In[61]:


pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)
print(last_names)


# In[118]:


list(reversed(range(10)))


# In[62]:


empty_dict = {}
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
d1


# In[64]:


d1[7] = 'an integer'
d1[6]=2.6
d1


# In[67]:


d1['b']


# In[68]:


'b' in d1


# In[69]:


d1[5] = 'some value'
d1


# In[70]:


d1['dummy'] = 'another value'
d1


# In[71]:


del d1[5]
d1


# In[72]:


ret = d1.pop('dummy')
ret


# In[128]:


d1


# In[129]:


list(d1.keys())


# In[73]:


list(d1.values())


# In[74]:


d1.update({'b' : 'foo', 'c' : 12})
d1


# In[75]:


mapping = dict(zip(range(5), reversed(range(5))))
mapping


# In[76]:


words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
by_letter


# In[137]:


by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
by_letter  


# In[138]:


from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
by_letter  


# In[79]:


print(hash('string'))

print(hash((1, 2, (2, 3))))

hash((1, 2, [2, 3]))


# In[83]:


d = {}
d[tuple([1, 2, 3])] = 5
d


# In[84]:


set([2, 2, 2, 1, 3, 3])


# In[85]:


{2, 2, 2, 1, 3, 3}


# In[86]:


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a.union(b)


# In[87]:


a | b


# In[88]:


a.intersection(b)
newset=a & b
newset


# In[7]:


c = a.copy()
c


# In[8]:


c |= b
c


# In[9]:


d = a.copy()
d &= b
d


# In[93]:


my_data = [1, 2, 3, 4]
my_set = {tuple(my_data)}
my_set
e = next(iter(my_set))


# In[94]:


a_set = {1, 2, 3, 4, 5}
{1, 2, 3}.issubset(a_set)


# In[95]:


a_set.issuperset({1, 2, 3,6})


# In[98]:


{1, 2, 3} == {3, 2, 1}


# In[101]:


strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lcs2=[x.upper() for x in strings if len(x) > 2]
lcs2


# In[102]:


unique_lengths = {len(x) for x in strings}
unique_lengths


# In[105]:


unique_lengths1 =set(map(len, strings))
unique_lengths1


# In[18]:


loc_mapping = {val : index for index, val in enumerate(strings)}
loc_mapping


# In[109]:


# Nested list comprehensions
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
all_data


# In[110]:


# To find names that have more than or equal to 2 character 'e' in there
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
names_of_interest


# In[111]:


# Another option
result = [name for names in all_data for name in names if name.count('e') >= 2]
result


# In[26]:


# “flatten” a list of tuples of integers into a simple list of integers
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened


# In[28]:


# Another option
flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
flattened


# In[29]:


# Convert a list of tuple to a nested list
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
[[x for x in tup] for tup in some_tuples]


# In[112]:


# Functions are the primary and most important method of code organization and reuse in Python.
def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)
    
result = my_function(5, 6, z=0.7)
result


# In[113]:


result = my_function(y=6, z=7, x=5)
result


# In[115]:


result =my_function(10,6)
result


# In[38]:


# When func() is called, the empty list a is created, five elements are appended, and then a is destroyed when the function exits.
def func():
    a = []
    for i in range(5):
        a.append(i)

b = func()
print(a,b)


# In[118]:


def func():
    for i in range(5):
        a.append(i)

a = []
b = func()
print(b,a)


# In[121]:


# global variables, generally discourage use of the global keyword.
def bind_a_variable():
    global a
    a = [6,5]

bind_a_variable()
print(a)


# In[2]:


# Returning Multiple Values, a 3-tuple
def f():
    a1 = 5
    b1 = 6
    c1 = 7
    return a1, b1, c1

a2, b2, c2 = f()
print (a2,b2,c2)


# In[9]:


# Returning Multiple Values, a dict
def f():
    a = 5
    b = 6
    c = 7
    return {'a' : a, 'b' : b, 'c' : c}
a1, b1, c1 = f()
print (a1,b1,c1)


# In[13]:


# Lots of things need to happen to make this list of strings uniform and
# ready for analysis: stripping whitespace, removing punctuation symbols, and standardizing
# on proper capitalization.

import re

states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

clean_strings(states)


# In[2]:


# Another way of doing so
import re

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result

states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']
clean_strings(states, clean_ops)


# In[4]:


# You can use functions as arguments to other functions like the built-in map function
for x in map(remove_punctuation, states): 
    print(x)


# In[9]:


# Anonymous (Lambda) Functions
def short_function(x):
    return x * 2


short_function(x)


# In[12]:


equiv_anon = lambda x: x * 2


# In[13]:


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)


# In[14]:


# To sort a collection of strings by the number of distinct letters in each string
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
strings


# In[27]:


# Currying: Partial Argument Application
def add_numbers(x, y):
    return x + y

y= 1
add_five = lambda y: add_numbers(5, y)
c=add_five(y)
c


# In[28]:


from functools import partial

add_five = partial(add_numbers, 5)
y= 1
c=add_five(y)
c


# In[29]:


# Generators: When you write for key in some_dict, the Python interpreter first attempts to create an iterator out of some_dict
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)


# In[30]:


dict_iterator = iter(some_dict)
list(dict_iterator)


# In[33]:


# A generator is a concise way to construct a new iterable object.
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2
        
gen = squares()
for x in gen:
    print(x, end=', ')


# In[34]:


# Generator expresssions
gen = (x ** 2 for x in range(100))


# In[35]:


def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()


# In[36]:


sum(x ** 2 for x in range(100))


# In[37]:


dict((i, i **2) for i in range(5))


# In[38]:


# itertools module: groupby takes any sequence and a function,
# grouping consecutive elements in the sequence by return value of the function

import itertools

first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator


# In[39]:


import itertools

first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Albert', 'Wes', 'Will','Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator


# In[41]:


# Errors and Exception Handling
float('1.2345')


# In[42]:


float('something')


# In[47]:


# a function that encloses the call to float in a try/except block
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x

attempt_float('1.2345')
attempt_float('something')
attempt_float((1, 2))


# In[50]:


f = open(path, 'w')

try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('Succeeded')
finally:
    f.close()


# In[61]:


path = 'C:/Users/aalaei/OneDrive - Southern Cross University/MyLapTop/SCU/MIT_Big_Data_Analysis_and_Tools/Designed Unit-S2-2020/Workshops/Examples_Book_Python for data analysis/segismundo.txt'
f = open(path)

lines = [x.rstrip() for x in f]
lines


# In[71]:


f.close()


# In[64]:


with open(path) as f: lines = [x.rstrip() for x in f]
lines


# In[66]:


f = open(path, 'rb')
f.read(10)


# In[67]:


f.tell()


# In[68]:


import sys
sys.getdefaultencoding()


# In[69]:


f.seek(3)


# In[70]:


f.read(1)


# In[72]:


# create a version of prof_mod.py with no blank lines
with open('tmp.txt', 'w') as handle: handle.writelines(x for x in open(path) if len(x) > 1)
with open('tmp.txt') as f: lines = f.readlines()
lines


# In[73]:


# Bytes and Unicode with Files: text or unicode characters
with open(path) as f: chars = f.read(10)
chars


# In[75]:


with open(path, 'rb') as f: data = f.read(10)
data


# In[76]:


data.decode('utf8')


# In[84]:


data[:4].decode('utf8')


# In[83]:


sink_path = 'C:/Users/aalaei/OneDrive - Southern Cross University/MyLapTop/SCU/MIT_Big_Data_Analysis_and_Tools/Designed Unit-S2-2020/Workshops/Examples_Book_Python for data analysis/sink.txt'
with open(path) as source:
    with open(sink_path, 'xt', encoding='iso-8859-1') as sink:
         sink.write(source.read())
with open(sink_path, encoding='iso-8859-1') as f: print(f.read(10))


# In[ ]:




