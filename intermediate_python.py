# INTERMEDIATE PYTHON NOTES
# OCTOBER 24, 2022

# LISTS
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
