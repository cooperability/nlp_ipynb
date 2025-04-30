#__________________________________________________________________________________________
#Classes in Python
#__________________________________________________________________________________________

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


#Classes can also be inherited:
class Bar(Foo):     #inherits variables and methods from above class
      pass

obj = Bar(3)
obj.print_x()     #3

# Line Comment

""""
Block Comment
"""

#_____________________________________________________________________________
#Int/Float/Bool Operations in Python
#_____________________________________________________________________________
var = 10
print(var + 4) 
print(var - 4) 
print(var * 4)

#Exponentiate: 
print(var ** 4)

#Float division: 
print(var / 4) 
#Integer division: 
print(var // 4)
#integer division is the same as dividing then casting, i.e. 
print(int(var / 4))
#Compound operators: 
var **= 4 
var += 1
#No increment or decrement using ++, -- in Python

print(not True) # prints False
print(True and False) # prints False
var = True or False
print(var) # prints True

# == checks value equality, 
# != checks inequality, 
# <= checks lequal, 
# >= checks grequal
#These things will evaluate to BOOL values, i.e. a <= b evaluates either true or false
#_____________________________________________________________________________

#Functions in python
#__________________________________________________________________________________________

def func(a, b): #define function
     pass #filler which quiets errors
#call function:
func(5, 10)

#optional parameters
def check_range(a, min_val = 0, max_val=10):   #create function to check if given number is in a range
      return min_val<a<max_val

check_range(5, max_val=3) #call the function

#immutable type parameters are passed by value. Ex:
def func(variable):
      variable=10
      print(variable)
a=15
print(a)  #outputs 15
func(a)  #outputs 10
print(a)  #outputs 15

#Mutable type parameters are passed by reference. Ex:
def func(variable):
     variable[0] = 10
     print(variable)
a=[0,1,2,3,4]
print(a)   #[0,1,2,3,4]
func(a)   #[10,1,2,3,4]
print(a)   #[10,1,2,3,4]

#circumvent mutability by creating a deep copy of your variable for your function:
def func(var):
     #alt 1
     var = var[:]
     #alt 2
     var=copy.deepcopy[variable]
     var[0]=10
     print(var)
a = [0,1,2,3,4]
print(a)     #[0,1,2,3,4]
func(a)     #[10,1,2,3,4]
print(a)     #[0,1,2,3,4]

#functions can access variables in their parent block's scope
outside_var="This is an outside variable!"
def func():
     print(outside_var)
print(outside_var)
func()

#functions can't change variables in their parent block's scope unless using the global key
outside_var = "This is an outside variable!"
def func():
     global outside_var
     outside_var = "Function changed the outside variable!"
print(outside_var) #"This is an outside variable!"
func()
print(outside_var)    #"Function changed the outside variable!"





#Defining functions within functions:
def main_function(a):
     def helper_func(a):
          return int(a)
     print(a)
     b=helper_func(a)
     print(b)

main_function(2.0)   
#2.0
#2

#Functions taking functions as variables:
def function_taker(a, func):
    return func(a)

function_taker(1.0, int)     #1

#Separately define passed function:
def parameter_function(x):
     return x+5
def function_taker(a, func):
     return func(a)
function_taker(1.0, parameter_function)  #6.0

#Lambda functions:
def function_taker(a, func):
     return func(a)
function_taker(1.0, lambda x: x + 5)  #6.0

#lambda functions can use variables in their parent's block scope:
num_to_add = 10
def function_taker(a, func):
     return func(a)
function_taker(1.0, lambda x: x + num_to_add)    #11

#Recursive functions:
def print_positive_numbers(num):
     if num <= 0:
          print("Done!")
     else:
          print(num)
          print_positive_numbers(num-1)

print_positive_numbers(10)  # prints positive numbers counting down from 10 one at a time

#can also inherit classes:
class Bar(Foo):
     pass

obj = Bar(3)
obj.print_x()     #3




#_____________________________________________________________________________
#String Operations in python
#_____________________________________________________________________________
#Comparison:
a = "221"; 
b='221'; 
print(a >= b); #returns True
#Length: 
a= "I love CS221!"; 
print(len(a)) #prints 13
#Element-Index: 
print(a[0]) #prints "I"
print(a[2:6]) #prints "love" (end-exclusive)
#To Lower/Upper: 
print(a.lower()) #prints "i love cs221!"
#Multiply: 
print(a * 4) #prints I love CS221!I love... 4 times
#Concatenate: 
b = "hbu?"; 
c = a + " " + b; 
print(c) #prints "I love CS221! hbu?"
#Contains: 
print("love" in a) #True 
print("love" not in a) #False 
print(a.index("love")) #2
#Split/Substring: 
print(a.split()) #prints ['I', 'love', 'CS221!'] or 
print(a.split('2')) #prints ['I love CS', ' ', '1!'] 
#The input here is the delimiter; the default delimiter is a space when input left blank
#When the input here is 2, the empty string returned is the string between the delimiters
#Split & combine a list:
a_splitted = a.split()
print(a_splitted) # ['I', 'love', 'CS221!']
a_joined = ' '.join(a.splitted)
print(a_joined) # I love CS221!
#Format/Dynamically call variables into strings
pi = 3.14159
print("Pi is %.2f!"%(pi)) #Pi is 3.14!  #"print me two decimals of pi as a floating point
print(f"Pi is {pi}!") #Pi is 3.14159! #f in front of string will refer to curly brackets & replace with variable


#_____________________________________________________________________________
#Variable Types in Python
#_____________________________________________________________________________
var = "hello" # str, immutable
print(type(var)) # prints "<class 'str'>"
#using double or single quotes to initialize strings has same behavior

var = 10 # int, immutable
print(type(var)) # prints "<class 'int'>"

var = 10.0 # float, immutable
print(type(var)) # prints "<class 'float'>"

var = True # False; Bool, Immutable - note CAPITALIZED
print(type(var)) # prints "<class 'bool'>"

var = (8,9) # tuple, immutable, collections of objects
print(type(var)) # prints "<class 'tuple'>"

var = [1, 2, 3] # list
print(type(var)) # prints "<class 'list'>"

var = None # None; replaces null
print(type(var)) # prints "<class 'NoneType'>"

#Variables can be cast to different types repeatedly
#Variable names are case-sensitive

#Assign values to multiple variables:
a, b, c = "I", "love", "CS221"
print(a, b, c) # I love CS221


#_____________________________________________________________________________
#Tuples in Python
#_____________________________________________________________________________
#immutable, hashable(can be used as dict key) lists of fixed size; no insertion or deletion
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


#_____________________________________________________________________________
#Iterables in python
#_____________________________________________________________________________
#immutable iterables, fixed size 
astring = str()
atuple = tuple()

#mutable iterables, not fixed size
alist=list() #linear
adict = dict()   #Hash table, stores (key, value) pairs
aset = set()     #hash table, like dict but only stores keys

#any iterable gives size with len(iterable)
print(len(alist))     #0

alist = [ ]    #initialize empty,, equivalent to list()
alist = [1, 2, 3, 4, 5]     #initialized list

#access & modify elements:
print(alist[0])    #1
alist[0] = 5     
print(alist)     #[5, 2, 3, 4, 5]
print("-"*10)
print(alist[-2])     #get last element at index len-1       #prints 4
print(alist[3:])     #get elements starting from index 3, inclusive      #prints [4, 5]
print(alist[:3])     #get elements stopping at index 3, exclusive     #prints [5, 2, 3]
print(alist[2:4])     #get elements within index range [2, 4]            #prints [3, 4]
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


#if list contains element:
if "new item" in alist:
     print("found")
else:
     print("not found")
#found


#_____________________________________________________________________________
#List Comprehension in Python
#_____________________________________________________________________________
#List Comprehension enables you to create new lists without a for-loop iterator. 

cities = ["NYC", "LA", "NOLA", "SF"]
newlist = [x for x in cities if "a" in x] = ["LA", "NOLA"]
newlist = [x for x in cities if x != "NYC"]
newlist = [x for x in range(10)]
newlist = [x.upper() for x in cities]
newlist = ['hola' for x in cities]
newlist = [x if x != "NOLA" else "Chicago" for x in cities] #replace "NOLA" with "Chicago" in output

print(newlist)


#_____________________________________________________________________________
#Sorting in Python
#_____________________________________________________________________________
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



#instead of lambda function, we can pass a function defined outside
def sorting_key(item):
     return item[1]
sorted(a, key=sorting_key)     #returns #[('cat', 1), ('bird', 2), ('dog', 3)]

#can sort dictionaries same way
adict = {'cat':3, 'bird':1}
print(sorted(adict.items(), key=lambda x:x[1]))  #sort by value; outputs [('bird', 1), ('cat', 3)]


#List Comprehension - replace for loops; unique to python
sent = ["nice day", "HELLO FRIEND"]
sent1 = [s.lower().split("  ") for s in sent]
print(sent1)     #[['nice', 'day'], ['hello', 'friend']]

#LC with conditionality
sent2 = [s.lower().split("  ") for s in sent if len(s)>8]
print(sent2)     #[['hello', 'friend']]

#create other iterables
keys = ['a', 'b', 'c']
dict1 = {k: i for i, k in enumerate(keys)}
print(dict1)      #{'a': 0, 'b': 1, ''c': 2}

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



#__________________________________________________________________________________________
#Control flows and Conditionals in Python
#__________________________________________________________________________________________
s="a"
#for-each loops for strings, arrays
for char in s:  #each char new line of print
     print(char)
for i, char in enumerate(a):  #chars now have line numbers in output
     print(i, char) 
#discrete for loops:
for i in range(4):   #same as for(int i=0; i<4; i++)
     print(i)
for i in range(2, -3, -2):   #same as for(int i=2; i> -3, i = -2)
     print(i)
#While loops
ind = 0
while ind < 5:
     print(ind)
     ind+=1
     break  #ends the loop
#If condition:
if str == "example":
     pass
elif str == "example2":
     pass
else:
     pass
#if None
a = None
if a: 
     pass
else: 
     print("None")
arr = [ ]
if arr: 
     pass
else:
     pass
str = ' '
if str: 
     pass
else:
     pass
if a is None: print('yes')







#________________________________________________________________________________________
#Dictionaries in Python (defaultdict, counter, set)
#__________________________________________________________________________________________


#store key-value pairs; not hashable; dynamic size; no duplicates allowed
#Hash-table implementation makes searching fast

adict = { }     #same as dict()
adict = {'dog': 10, 'bird': 5, 'lion': 8}
print(adict)     #{'dog': 10, 'bird': 5, 'lion': 8}

print(adict.keys())     #dict_keys(['dog', 'bird', 'lion'])
print(adict.values())     #dict_values([10, 5, 8])
print(adict.items())     #dict_items([('dog', 10), ('bird', 5), ('lion', 8)])

#access by key
print(adict['lion'])     #8

#check if key exists
adict['tiger']    #throws error
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


#_____________________________________________________________________________
#Terminal Commands in Python
#_____________________________________________________________________________
#Python:
#activate python using python; quit with quit()
#can check paths with import sys and then print(sys.path)
#Set Version: python global <version> i.e. "python global 3.8.11"; can be replaced for local
#Create Virtual Environment: $ pyenv virtualenv <python_version> <environment_name>
#pyenv which python; pyenv which pip; pyenv versions
#pyenv activate <environment_name>; pyenv deactivate
#python example.py - runs executable py
#which python
#PIP
#Add package: python -m pip install scipy
#Upgrade Package: pip install --upgrade torch torchvision
#List packages: pip list, pip freeze
#Show package location: pip show <package-name>
#pip freeze > requirements.txt will create the requirements.txt file from your django folder
#Conda
#Use the base environ through conda and build other environments on top
#conda list shows installed packages
#Poetry
#"poetry init" creates a pyproject.toml file with a poetry section, or tells you if one already exists
#"poetry install" creates your virtual environment and installs dependencies in it from the lockfile
#"poetry env info" will show you the current environment you're working in
#"poetry env info -p" shows the path to your current environment
#"poetry env list" shows all active environments
#"poetry env remove --all" does what it says
#"poetry add [packegename]" or "poetry remove [packagename]" does what it says on the tin
#"poetry shell" opens a specified poetry shell for your current environment
#to exit type "exit"
#"poetry config virtualenvs.in-project true" sets a default that your created virtual environments will be created INSIDE the project folders where the pyproject.toml file is stored
#after this stage, "poetry install" should run virtual env creation in your folder itself
#$ poetry export -f requirements.txt -o requirements.txt --without-hashes
#`scrapy crawl [spidername]` will run the desired spider in its .py file

#_____________________________________________________________________________
#ScraPy Terminal Commands
#_____________________________________________________________________________
#scrapy startproject [projectname]
#scrapy genspider [spidername] [domainToScrape]
#scrapy list to show all spiders
#scrapy shell “root-domain.url”
#scrapy crawl [spidername] [-O for output, then filename.type]
#fetch(’<url>’)
#targetVar = response.css(’pageComponentClassName’); → retrieve all items of the specified class name
#“” = response.xpath(“//component[@class=‘className’]/text()”).extract()
#“”=response.css(“a”).xpath(“@href”).extract()
#targetVar = response.css(’””’).get() → return only first item in set’s HTML
#product.css(’a.product-item-meta__title::text’).get()
#product.css(’span.price’).get().replace(’<div>unwanted html</div>’ , ’’).replace(’<div>unwanted html</div>’ , ’’) → remove dirty html from result
#product.css(’div.product-item-meta a’).attrib[’href’] → retrieve only single attribute value from desired object
#response.css(’[rel=”next”] ::attr(href)’).get() → fetch only the href attribute from only elements with the rel=”next” tag




#_____________________________________________________________________________
#Regexes in Python
#_____________________________________________________________________________
#"in" operator evaluates to a truth value for substrings e.g.
#"hat" in "five hundred hats"? --> True
#"[desired number]" in "patient cellphone: [desired number]" --> True

#Regexes allow us to search for similarly formatted pattern searching in a text document
#Regex to search for a phone number: 
r'\d{3}-\d{3}-\d{4}'

#Every character type has a pattern code, e.g.
#\d for digits, as in the above phone number
#\w for alphanumeric, e.g. \w-\w\w\w = A-b_1
#\s for White space, e.g. a\sb\sc = a b c
#\D for non-digit, e.g. \D\D\D = ABC
#\W for non-alphanumeric, e.g. \W\W\W = *+_
#\S for non-whitespace e.g. \S\S\S\S = yoyo
#. for wildcard, can be any character

#Quantifiers have pattern codes, e.g.
#+ : occurs one or more times
#{num} : occurs num times
#{num1,num2}: occurs between num1 and num2 times
#{num,} : occurs num or more times
#* : occurs zero or more times
#? : occurs once or zero times
#\d$ for "ends with \d", ^\d for "starts with \d" 
#square bracket anything which you want to exclude

#example:
#r'[^a-zA-Z0-9]'
#r'[^a-zA-Z0-9]'

