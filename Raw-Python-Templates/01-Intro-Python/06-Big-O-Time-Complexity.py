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
"""
Big-O notation measures how a function's time-to-output, or time-to-completion, 
scales proportionally with the size of an input, represented by n. If input size
n is plotted on the x-axis, time-to-completion O(n) is plotted on the y-axis. 

The O stands for "order of complexity". 
Big-O can be described as "how code slows as data grows".

Big-O is pessimistic and takes the worst-case scenario, or fastest-growing O(n), as 
the runtime. For example, O(n + n log(n)) reduces to O(n log(n)) since this is the 
biggest term of the two, and if you're inserting a value into an array, you assume it 
will be inserted in the worst(first) index, and that all other values must be shifted 
over. Therefore, even though there is a possible situation where a value is appended, 
requiring no existing values to change indices, we assume each time we operate that 
the value must be added to the first index, requiring all existing values to change indices.

Big-O also ignores all constants in favor of directly describing the relationship between
n and O(n).

Several tutorials made this possible:
https://www.youtube.com/watch?v=BgLTDT03QtU
"""
import matplotlib.pyplot as plt
import math
x=[0,1,2,3,4,5,6,7,8]

one=[None]*len(x)
logn=[None]*len(x)
n=[None]*len(x)
nlogn=[None]*len(x)
nsquared=[None]*len(x)
ncubed=[None]*len(x)
twotothen=[None]*len(x)
sqrtn=[None]*len(x)

for i in range(1, len(x)):
    one[i]=1
    logn[i]=math.log(i)
    sqrtn[i]=math.sqrt(i)
    n[i]=i
    nlogn[i]=i*math.log(i)
    nsquared[i]=i**2
    ncubed[i]=i**3
    twotothen[i]=2**i

plt.title("O(n) Complexities")
plt.xlabel("Input Size(n)")
plt.ylabel("Time-To-Completion (O(n))")
plt.plot(x,one,label='O(1)')
plt.plot(x,logn,label='O(log(n))')
plt.plot(x,sqrtn,label='O(sqrt(n)')
plt.plot(x,n,label='O(n)')
plt.plot(x,nlogn,label='O(n*log(n))')
plt.plot(x,nsquared,label='O(n^2)')
plt.plot(x,ncubed,label='O(n^3)')
plt.plot(x,twotothen,label='O(2^n)')

ax=plt.gca() #Get current axis
ax.set_ylim([0,30])
plt.legend()
plt.show()

# +
"""
O(1) does not scale time-to-completion with input WHATSOEVER
e.g. appending/removing a single new value to/from a struct, 
popping the most recent value added to a struct, 
removing a value from a struct, 
inserting a value at the beginning of a linkedlist,
or looking up an entry in a struct by index (also looking up an item by key in a hashMap). 

Also qualifying for O(1) is the Gaussian equation for the sum of numbers under a given num.
"""
nums=[1,2,3]
nums.append(4) #O(1) to push to end
print("Array output:")
print(nums.pop()) #O(1) to pop from end
print(nums[0]) #O(1) to lookup
print(nums[1]) #O(1)
print(nums[2]) #O(1)

hashMap = {
    "1": "Sachin Tendulkar",
    "2": "Dravid",
    "3": "Sehwag",
    "4": "Laxman",
    "5": "Kohli"
}
hashMap["key"]="Coop" #O(1) to insert
print("\nhashMap output:") 
print("key" in hashMap) #O(1) to lookup
print(hashMap["key"]) #O(1) to lookup
hashMap.pop("key") #O(1) to remove

def sum(n): #No matter the input, this will run in 3 steps
    s = (n * (n+1))/2
    return s
print("\nSums of numbers under 5, 10, 15:")
print(sum(5))
print(sum(10))
print(sum(15))
# -

"""
O(log n) scales at a speed between O(1) and O(n); MUCH smaller than O(n) and closer to O(1)
e.g. binary search; halves the size of the structure being searched after each run
"how many times can you divide n by 2 until it equals one?"
"How many times can you multiply 1 by two until it's equal to n? Two to the power of x 
equals n, so x(time to complete) must be equal to log n."
"""
print("Binary search on Array:")
nums=[1,2,3,4,5]
target=5
l,r=0,len(nums)-1
while(l<=r):
    m=(l+r)//2
    if target<nums[m]:
        r=m-1
        print(f"right updated to {r}")
    elif target>nums[m]:
        l=m+1
        print(f"left updated to {l}")
    else:
        print(f"found target at {m}")
        break

"""
O(sqrt(n)) scales between O(log n) and O(n), e.g. "get all factors of n" only reviews
potential values which are LESS than the square root of n
"""
import math
n=12
factors=set()
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        factors.add(i)
        factors.add(n//i)
print(factors)

# +
"""
O(n), or "linear time/complexity", scales time-to-completion linearly with input of size n
A single for-each loop, while-true loop or other iterable which checks every value in
a struct has O(n) runtime. 

Search, Insert, Remove from an array, and searching through a linkedlist, all have O(n).

Inserting or removing a value from the MIDDLE of an n-size array has O(n), since 
pessimistically all other array values must be relocated. If removing a value 
from the end, it's an O(1) operation; if removing from the beginning, it's O(n)
Heapify and monotonic stack also require O(n), even when they have nested iterable loops
"""
nums=[1,2,3]
print(sum(nums)) #O(n) to iterate through all values and sum
for n in nums: #O(n) to read each value
    print(n)
    
nums.insert(1,100) #O(n) to insert item in middle; assume O(n) for all inserts
nums.remove(100) #O(n) to remove item from middle; assume for all removals
print(100 in nums) #O(n) to search

import heapq
heapq.heapify(nums) #O(n) to build heap

#SOME nested loops such as monotonic stack and sliding window have O(n)
# -

"""
O(n log n), or "quasilinear time" is only barely less efficient than O(n), and MUCH 
more efficient than O(n^2)
quicksort, mergesort and heapsort are quasilinear, as are MOST built-in sort functions
Heap sort(below) is technically O(n + n log n), but we take the bigger term and reduce 
its complexity to O(n log n) pessimistically.
This is the first level of complexity which begins to slow down exponentially with larger
datasets; observe this in the graph at the start of the notebook.
"""
#heapsort
import heapq
nums=[1,2,3,4,5]
heapq.heapify(nums) #O(n)
while nums:
    heapq.heappop(nums) #O(log n)

# +
"""
O(n^2) or "quadratic time" scales time-to-completion quadratically with n-size input
Nested for-loops, iterating through a n*n grid row-column style, iterating through a size-n 
struct n times all have O(n^2) runtime
e.g. insertion sort inserts into the middle of the array n times, or getting every PAIR of 
elements in an array.
Insertion sort, selection sort, and bubble sort all belong here
If iterating through all spots of an n-size array, then all spots minus the first, then all 
spots minus the first two etc., this will have O(n^2 /2), but constants aren't considered, 
so this problem has O(n^2)
"""
print("Print all objects from 2d Array in O(n^2):")
nums=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nums)):
    for j in range(len(nums[i])): #nested for loops will have O(n^2) runtime
        print(nums[i][j])
        
print("\nGet pairs of elements in 1d Array in O(n^2):")
nums=[1,2,3]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        print(nums[i], nums[j])

# +
#O(n*m) is similar to O(n^2), but the struct is not square.
# -

"""
O(n^3) is where algorithms become much less common, but might still be encountered
Three nested loops will do this
e.g. finding every possible TRIPLET of values in an array
"""
nums=[1,2,3,4,5]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            print(nums[i], nums[j], nums[k])

# +
"""
O(2^n) is a reflection of O(log n) about the y=x line, and is most commonly encountered 
in recursion
"""
#tree height n, two branches: O(2^n)
nums=[1,2,3,4,5]
i=0
def recursion(i,nums):
    if i==len(nums):
        print("returning 0")
        return 0
    branch1=recursion(i+1, nums)
    branch2=recursion(i+2, nums)
    
#c branches, where c is sometimes n
def recursion(i, nums, c):
    if i==len(nums):
        return 0
    for j in range(i, i+c):
        branch=recursion(j+1, nums)


# -

"""
O(n!) is pretty rare, but comes up in permutations and the Travelling Salesman Problem.
Generally O(n!) is enormously inefficient, but sometimes necessary.
Also notable is that BOGO sort is O((n+1)!)
"""
