**immutable**: str, int, float, bool, tuple || **Mutable**: List, Dict, Set

**\*\*** exponentiates; **/** divides to float; **//** divides & rounds down to whole

********\*\*********f-string********\*\*********: Dynamic load f”{var}” **|** ********\*\*********substring:********\*\********* stringname[start:end:step]

```python
#named tuples improve readability
from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1  = Point(1.0, 5.0)
```

**********\*\*\*\***********Dictionaries**********\*\*\*\*********** are mutable, traversable, insertable, iterable

```python
from collections import defaultdict
adict = defaultdict(lambda: 'unknown')
adict['cat'] = 'feline'
print(adict['cat'])     #feline
print(adict['dog'])     #unknown
```

**\*\***Lambda**\*\*** functions can take any number of args, but return 1 expression

Best for prototyping multi-use functions with different contexts

def myfunc(n): return lambda a : a \* n

mydoubler = myfunc(2) ; print(mydoubler(11))

mytripler = myfunc(3) ; print(mytripler(11))

```python
#lambda functions can use variables in their parent's block scope:
num_to_add = 10
def function_taker(a, func):
     return func(a)
function_taker(1.0, lambda x: x + num_to_add)    #11
```

******\*\*\*\*******O(log n)******\*\*\*\*******: Binary Search. **\*\*\*\***O(n)**\*\*\*\***: array search, insert, remove
