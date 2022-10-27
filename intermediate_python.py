# INTERMEDIATE PYTHON NOTES
# OCTOBER 24, 2022

# LISTS
from cProfile import label
from dataclasses import dataclass
import re


x = ['hi', 'hello', 'welcome']

# DICTIONARIES
"""
    DICTIONARIES ARE ANOTHER COLLECTION TYPE AND
    ALLOW YOU TO MAP ARBITRARY KEYS TO VALUES.

    DICTIONARIES CAN BE INDEXED IN THE SAME WAY
    AS LISTS, USING SQUARE BRACKETS CONTAINING KEYS.

"""

ages = {
    "Dave": 24,
    "Mary": 42,
    "John": 58
}

print(ages['Dave'])
print(ages['Mary'])

"""
    ONLY IMMUTABLE OBJECTS CAN BE USED AS KEYS TO 
    DICTIONARIES. IMMUTABLE OBJECTS ARE THOSE THAT 
    CAN'T BE CHANGED.

EXAMPLE: 
bad_dict = {
    [1, 2, 3] = "one two three"
}

"""

# DICTIONARY FUNCTIONS 

nums = {
    1: "one",
    2: "two",
    3: "three",
}

print(1 in nums)
print("three" in nums)
print(4 not in nums)

# DICTIONARY FUNCTION ".get(value, alternative_value)"

"""
    Return an alternative value, if the specified value 
    is not found.
"""

pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

# TUPLES

"""
    Tuples are very similar to lists, except that they
    are immutable(cannot be changed).
    Tuple = ()
"""

words = ("spam", "eggs", "sausages")

"""
    Can be indexed but cannot be reassigned.
"""

print(words[0])

#words[1] = "cheese" # Causes a TypeError

print(words)

"""
    Tuples can be created without the parentheses by just
    seperating the values with commas.

"""

my_tuple = "one", "two", "three"

print(my_tuple)

"""
    Tuples are faster than lists, but they cannot be changed.

"""

# TUPLE UNPACKING

"""
    Tuple unpacking allows you to assign each item to a variable.

"""

numbers = (1, 2, 3)

a, b, c = numbers

print(a, b, c)

"""
    A variable that is prefaced with an asterisk (*) takes all values
    from the collection that are left over from the other variables.

"""

a, b, *c, d = [1, 2, 3, 4, 6, 7, 8, 9]

print(a, b, c, d)

# SETS 

"""
    Sets are similar to lists or dictionaries.
    {}
    unordered = cannot be indexed.
    Sets cannot contain duplicate elements.

"""

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

"""
    Sets can be combined using mathematical operations.
    | Union Operator - combines two sets to form a new one
                containing items in either.
    & Intersection Operator - gets items only in both.
    - Difference Operator - gets items in the first set but 
                not in the second.
    ^ Symmetric Difference - gets items in either set, but
                not both.

"""

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

# LIST COMPREHENSION 

"""
    Lists comprehensions are a useful way of quickly creating 
    lists whose contents obey a rule.

"""

cubes = [i**3 for i in range(5)]
print(cubes)

"""
    A list comprehension can also contain an if statement to enforce a
    condition on values in the list.

"""

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

# FUNCTIONAL PROGRAMMING

"""
    Functional Programming is a style of programming that is based around 
    functions.

    A key part of functional programming is higher-order functions. Higher
    -order functions take other functions as arguments, or return them as 
    results.
"""

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

def add_two(x):
    return x + 2

print(apply_twice(add_five, 10))
print(apply_twice(add_two, 0))

# PURE FUNCTIONS

"""
    Functional programming seeks to use pure functions. Pure functions have
    no side effects, and return a value that depends only on their 
    arguments. 
"""

# PURE FUNCTION

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# IMPURE FUNCTION

some_list = []

def impure(arg):
    some_list.append(arg)

print(pure_function(10, 5))

impure(5)
impure(2)
impure(7)

print(some_list)    

# PURE FUNCTIONS

"""
    Using pure functions has both advantages and disadvantages. 
    Pure functions are:
        - easier to reason about and test.
        - more efficient. Once the function has been evaluated for an input,
        the result can be stored and referred to the next time the function
        of that input is needed, reducing the number of times the function
        is called. This is called memoization.
        - easier to run in parallel. 

    Pure functions are more difficult to write in some situations.
"""

# LAMBDAS

"""
    Creating a function normally (using def) assigns it to a variable with
    its name automatically.

    Python allows us to create functions on-the-fly, provided that they are
    created using lambda syntax.
"""

def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x, 5))

"""
    Functions created using the lambda syntax are known as anonymous.

    Lamda functions aren't as powerful as named functions.

    They can only do things that require a single expression -- usually
    equivalent to a single line of code.
"""

# NAMED FUNCTION
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

# LAMBDA
print((lambda x: x**2 + 5*x + 4) (-4))

# MAP

"""
    The built-in functions map and filter are very useful higher-order 
    functions that operate on lists (or similar objects called iterables).

    The function map takes a function and an iterable as arguments, and
    returns a new iterable with the function applied to each argument.
"""

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))

print(result)

# USING LAMBDAS

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

result_y = (lambda y: y**3) (2)

print(result_y)

nums = [11, 22, 33]

a = list(map(lambda x: x*5, nums))

print(a)

# FILTER

"""
    The function filter filters an iterable by leaving only the items that 
    math a condition (also called a predicate)
"""

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
