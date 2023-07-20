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

#sort iterables
a = [4,6,1,7,0,5,1,8,9]
a = sorted(a)
print(a)     #[0,1,1,4,5,6,7,8,9]
a = sorted(a, reverse=True)
print(a)      #[reverse of above lol]

#sort iterables containing tuples
a = [("cat", 1), ("dog", 3), ("bird", 2)]
a = sorted(a)
print(a)     #[('bird', 2), ('cat', 1), ('dog', 3)]
b = sorted(a, key=lambda item: item[1])   #sort by value instead of by key
print(b)     #[('cat', 1), ('bird', 2), ('dog', 3)]

# +


#instead of lambda function, we can pass a function defined outside
def sorting_key(item):
     return item[1]
sorted(a, key=sorting_key)     #returns #[('cat', 1), ('bird', 2), ('dog', 3)]
# -

#can sort dictionaries same way
adict = {'cat':3, 'bird':1}
print(sorted(adict.items(), key=lambda x:x[1]))  #sort by value; outputs [('bird', 1), ('cat', 3)]

# +

#List Comprehension - replace for loops; unique to python
sent = ["nice day", "HELLO FRIEND"]
sent1 = [s.lower().split("  ") for s in sent]
print(sent1)     #[['nice', 'day'], ['hello', 'friend']]
# -

#LC with conditionality
sent2 = [s.lower().split("  ") for s in sent if len(s) >8]
print(sent2)     #[['hello', 'friend']]

#create other iterables
keys = ['a', 'b', 'c']
dict1 = {k: i for i, k in enumerate(keys)}
print(dict1)      #{'a': 0, 'b': 1, ''c': 2}

# +
#zip function takes two same-length lists and returns a zip object, which can then be relisted as a list of key-value pairs from those two lists
keys=['a', 'b', 'c']
values = [10, 5, 30]
zipped = zip(keys, values)
print(zipped)     #zip object
print(list(zipped))     #pass to list to unzip

for k, v in zip(keys, values):
     print(k, v)
        
        #output:
#<zip object at 0x7fa255783960>
#[('a', 10), ('b', 5), ('c', 30)]
#a 10
#b 5
#c 30
# -


