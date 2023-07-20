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

# +
class Foo: #if "class Foo(object): all python classes will inherit 'object'
       class_variable = 'same'
       def __init__(self, x):      #optional constructor; required for some classes
            self.x = x     #first parameter "self" for instance reference, like "this" in java
       def print_x(self): #instance reference is required for all instance variables
            print(self.x)
       @classmethod
       def modify_class_variable(cls):
            cls.class_variable = 'changed'
       @staticmethod
       def print_hello():
            print("Hello!")

print(Foo.class_variable)  #same
obj1=Foo(6)  
obj1.print_x()    #6
print(obj1.class_variable)     #same

obj2 = Foo(5) 
obj2.print_x()     #5
print(obj2.class_variable)     #same

obj1.modify_class_variable()
print(obj1.class_variable)     #changed
print(obj2.class_variable)     #changed
print(Foo.class_variable)      #changed


# +
#Classes can also be inherited:
class Bar(Foo):     #inherits variables and methods from above class
      pass

obj = Bar(3)
obj.print_x()     #3

# +
"""
ITERABLES & LOOPS
"""
#immutable iterables, fixed size 
astring = str()
atuple = tuple()

#mutable iterables, not fixed size
alist=list() #linear
adict = dict()   #Hash table, stores (key, value) pairs
aset = set()     #hash table, like dict but only stores keys

#1. any iterable gives size with len(iterable)
print("Output 1:")
print(len(alist))     #0

alist = [ ]    #initialize empty,, equivalent to list()
alist = [1, 2, 3, 4, 5]     #initialized list

#2. access & modify elements of a data structure:
print("Output 2:")
print(alist[0])    #1
alist[0] = 5     
print(alist)     #[5, 2, 3, 4, 5]
print("-"*10)
print(alist[-2])     #get last element at index len-1       #prints 4
print(alist[3:])     #get elements starting from index 3, inclusive      #prints [4, 5]
print(alist[:3])     #get elements stopping at index 3, exclusive     #prints [5, 2, 3]
print(alist[2:4]     #get elements within index range [2, 4]            #prints [3, 4]
print(alist[len(alist):])       #prints nothing, index out of range     #prints [ ]

#reverse a list
alist[::1] # returns [5, 4, 3, 2, 5]

#list methods:
alist.append("new item")     #insert at end
alist.insert(0, "new item")      #insert at index 0
alist.extend([2, 3, 4])       #concatenate lists; equivalent to alise += [2, 3, 4]
alist.index("new item")     #search by content
alist.remove("new item")     #remove by content
popped = alist.pop(0)     #remove by index
print(alist)     #[2, 3, 4, 5, 'new item', 2, 3, 4]
print(popped)      #5


#5. if list contains element:
print("block 5:")
if "new item" in alist:
     print("found)
else:
     print("not found")
#found

# -


