# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

#output and formatting
#In python, lines in the same code block must have identical indentation
"""
Here's a block comment.
"""
print("hola mundo")

#variable types: string, int, float, bool, tuple, list, none
s = "hello" #string; immutable; can use double or single quotes
i = 10 #int; immutable
f = 10.0 #float; immutable
b = False #bool; immutable - must be capitalized
t = (3,4) #tuple; immutable; any size collection
l = [1,2,3] #list; mutable
n = None #none replaces null
print(f"{type(s)},\n {type(i)},\n {type(f)},\n {type(b)},\n {type(t)},\n {type(l)},\n {type(n)}")

#setting multiple variables at once
a, b, c = "I'm feeling rough,", "I'm feeling raw, \n", "I'm in the prime of my life"
print(a, b, c)

# +
#Int/Float/Bool Operations

i = 10 #int add, subtract, multiply, divide, exponentiate
print(f"int={i}; i+4={i+4}, i-3={i-3}, i*5={i*5}, i/2={i//2}, i^2={i**2}")

f = 10.0 #float
print(f"float={f}; f/2.5={f/2.5}, f^2.0={f**2.0}")
#dividing a float by an integer is the same as dividing then casting, i.e. int(f/4)
#can't increment or decrement with ++ or -- in python

#compound operators update values in one line
f+=1.0
print(f"f+1.0={f}")
f**=2.0
print(f"f^2.0={f}")

#compound bools have predictable truth-values
print(f"not True={not True}, True and False={True and False}, True or False={True or False}")

#inequalities: equals, not equals, greater than, lesser than
print(f"1==1.0:{1==1.0}, 1!=1.0:{1!=1.0}, 1<=2:{1<=2}, 1>=2:{1>=2}")

# +
#1. string Operations: comparison, length, element-index, upper/lower
#use "f-strings" in the format f"var={var}" to dynamically load variables
a, b, c = "2890", '2890', "I'm in the prime of my life"
print(f"1. a>=b:{a>=b} \nlength(c):{len(c)} \nc[11]={c[11]} \nc[1].lower()={c[0].lower()}")

#2. multiply, concatenate, in(contains), index
print(f"\n\n2. a*4={a*4} \na+' '+c={a+' '+c} \n'life' in c={'life' in c} \nc.index('life')={c.index('life')}")
      
#3. split-by-delimiter, substring
#default split() delimiter is space; will return an empty string between two adjacent delimiters
#substring uses stringname[start:end:step] formatting, where step indicates skipped characters
c_split=c.split('m')
c_join='m'.join(c_split)
sub_c=c[10:25:1]
sub_c_2split=c[10:25:2]
print(f"\n\n3.c.split('m')={c_split} \nc_split[1]={c_split[1]} \n'm'.join(c_split)={c_join}")
print(f"sub_c={sub_c} \nsub_c_2split={sub_c_2split}")


# +
"""
Tuples in Python:
immutable, hashable(can be used as dict key) lists of fixed size; no insertion or deletion
"""
atuple = (1,2,3,4,5)
atuple = (1,)       #need comma for singleton atuple, otherwise defaults to integer

#index/traverse same as list
atuple=tuple([1,2,3])

#use as dictionary keys
ngram = ("a", "cat")
d = dict()
d[ngram] = 10
d[ngram] += 1

#named tuples improve readability
from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1  = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
print(pt1.x, pt1.y)     #1.0 5.0

# +
"""
Dictionaries in Python:
store key-value pairs; not hashable; dynamic size; no duplicates allowed
Hash-table implementation makes searching fast
"""

adict = { }     #same as dict()
adict = {'dog': 10, 'bird': 5, 'lion': 8}
print(adict)     #{'dog': 10, 'bird': 5, 'lion': 8}

print(adict.keys())     #dict_keys(['dog', 'bird', 'lion'])
print(adict.values())     #dict_values([10, 5, 8])
print(adict.items())     #dict_items([('dog', 10), ('bird', 5), ('lion', 8)])

#access by key
print(adict['lion'])     #8

#check if key exists
#adict['tiger']    #throws error
if 'tiger' in adict:
     print(adict[key])
else:
     print("key not found")    # key not found

#insert new keys
adict['tiger'] = 1

#modify existing
adict['lion'] = 20

#traverse dictionaries
for key in adict:
     print(key, adict[key])
#dog 10
#bird 5
#lion 8
#tiger 1

#Traverse key-value pairs together
for key, val in adict.items():
     print(key, val) #same output as above lol

#DefaultDict is a special dictionary returning a default value when a queried key doesn't have one to match.
from collections import defaultdict
adictr = defaultdict(int)
adict['cat'] = 5
print(adict['cat'])     #5
print(adict['dog'])     #0

#you can also pass a custom function:
from collections import defaultdict
adict = defaultdict(lambda: 'unknown')
adict['cat'] = 'feline'
print(adict['cat'])     #feline
print(adict['dog'])     #unknown

#counters are dicts with default value 0.
from collections import Counter
counter1 = Counter()
counter1['t'] = 10
counter1['t'] += 1
counter1['e'] += 1
print(counter1)     #Counter({'t' : 11, 'e' : 1})

#initialize counters from other iterables:
counter2 = Counter("letters to count")
print(counter2)     # long output but it logs all letters with corresponding counts

#operations between counters
print("1", counter1 + counter2)     # prints 1, then sum of both letter counts together
print("2", counter1 - counter2)   #prints 2, then Counter({'t': 7}), the difference between the two sets
print("3", counter1 or counter2)  #or for union, and for intersection

#last Counter Methods
counter2.most_common(5)   #prints 5 most common values of that counter plus keys
for k, v in counter2.most_common(5):
     print(k, v)


#Set is special dictionary without values & no repetitions
aset = set()
aset.add('a')
alist = [1,2,3,3,3,4,3]
alist = list(set(alist))
print(alist)           #[1,2,3,4]
# -


