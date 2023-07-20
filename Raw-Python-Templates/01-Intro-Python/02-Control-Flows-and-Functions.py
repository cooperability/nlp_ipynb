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

#for-each loops for strings & arrays
s="where's the beef?"
for char in s:
    print(char)
for i, char in enumerate(s): #add line numbers in output
    print(i, char)
for i in range(4): #alternate: for(int i=0; i<4; i++)
    print(i)
for i in range(2, -3, -2): #alternate: for(int i=2; i> -3; i-=2)
    print(i)

#while loops, bonus elif if-else structure
ind=0
while ind<5:
    if(ind % 2==1):
        print(f"{ind} is odd")
    elif(ind > 3): 
        break
    else:
        print(ind)
    ind += 1

# +
#none-checking
a=None
b=[]
c=''
if a or b or c:
    print("it exists")
else:
    print("it don't exist")
    
if a is None:
    print("it's None")
    

# +
#define functions
def func(a,b): #junk function
    pass #quiets errors
func(5,10)

def check_range(a, min_val=0, max_val=10): #is a in the given range?
    print(min_val<a<max_val)
check_range(5, 4, 6)
check_range(5, max_val=3) #optional parameters can be omitted



# +
#parameters of immutable type are passed by value.
print("pass immutables by value:")
def func(var):
    var=10
    print(var)
a=15
print(a)
func(a)
print(a)

#parameters of mutable types are passed by reference.
print("\nPass mutables by reference:")
def f(v):
    v[0]=10
    print(v)
a=[0,1,2,3,4]
print(a)
f(a)
print(a)


# -

#circumvent mutability by creating a deep copy of your variable for your function
def func(var):
    var=var[:] #option 1
    v=copy.deepcopy(var)
    v[0]=10
    print(v)
a=[0,1,2,3,4]
print(a)
func(a)
print(a)

"""
SCOPING VARIABLES
"""
#1. functions can access variables scoped to their parent's block
print("Function 1:")
outside_var="This is an outside variable!"
def func():
     print(outside_var)
print(outside_var)
func()

#2. but functions can't change variables in their parent block's scope,
#unless using the global key
print("\nfunction 2:")
outside_var2 = "This isn't scoped for the function"
def func2():
    global outside_var2
    outside_var2="Function changed the variable!"
print(outside_var2)
func2()
print(outside_var2)

#3.variables defined in function scope can only be accessed outside using global key
#this is bad form and officially recommended against:
print("\nfunction 4:")
def foo():
     global g_v #if you printed after this line, undefined error
     g_v="This is global var!"
     print(g_v)
def bar():
     print(g_v)
foo() #This is global var!
bar() #This is global var!

#if a same-name variable is function-scoped, the later definition overwrites the former 
#only in that scope
print("\nfunction 4:")
var="outside var!"
def func(var="func var"):
     print(var)
print(var) #outside var!
func()  #func var
print(var) #outside var!


# +
#1. Defining functions within functions:
def main_function(a):
     def helper_func(a):
          return int(a)
     print(a)
     b=helper_func(a)
     print(b)

main_function(2.0)   
#2.0
#2

# +
#2. Functions taking functions as variables:
def function_taker(a, func):
    return func(a)

function_taker(1.0, int)     #1

# -

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
print_positive_numbers(8)


