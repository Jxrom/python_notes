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

# GENERATORS

"""
    Generators are a type of iterable, like lists or tuples.
    Unlike lists, they don't allow indexing with arbitrary indices, but 
    they can still be iterated through with for loops.

    They can be created using functions and the yield statement.
"""

def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

def add_num():
    for i in range(20):
        yield i 
        i += 1
        print(i)

print(add_num())
 
def five(x):
    for i in range(20):
        yield 5 * x

for i in five(2):
    #print(i)
    pass

"""
    Finite generators can be converted into lists by passing them as 
    arguments to the list function.
"""

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

"""
    Using generators results in improved performance, which is the 
    result of the lazy (on demand) generation of values, which translates
    to lower memory usage. Furthermore, we do not need to wait until all 
    the elements have been generated before we start to use them.
"""

def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word
    
print(list(make_word()))    

# DECORATORS

"""
    Decorators provide a way to modify functions using other functions.
    This is ideal when you need to extend the functionality of functions
    that you don't want to modify.
"""

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

"""
    We defined a function named decor that has a single parameter func.
    Inside decor, we defined a nested function named wrap. The wrap function
    will print a string, then call func(), and print another string. The
    decor function returns the wrap function as its result.

    We could say that the variable decorated is a decorated version of print_
    text - it's print_text plus something.

    In fact, if we wrote a useful decorator we might want to replace print_text
    with the decorated version altogether so we always got our "plus something"
    version of print_text.

    This is done by re-assigning the variable that contains our function.
"""

print_text = decor(print_text)
print_text()

"""
    In our previous example, we decorated our function by replacing the variable
    containing the function with a wrapped version.
"""

def print_text():
    print("Hello world!")

print_text = decor(print_text)

"""
    This pattern can be used at any time, to wrap any function.
    Python provides support to wrap a function in a decorator by pre-pending
    the function definition with a decorator name and the @symbol.
    If we are defining a function we can "decorate" it with the @ symbol like:
"""

@decor
def print_text():
    print("Hello World!")

print_text()

# RECURSION

"""
    Recursion is a very important concept in functional programming. The fundamental
    part of recursion is self-reference -- functions calling themselves.

    It is used to solve problems that can be broken up into easier 
    sub-problems of the same type.
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial(5))

"""
    Recursion can also be indirect. One function can call a second, which
    calls the first, calls the second, and so on. This can occur with any
    number of functions.
"""

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))
print(is_even(22))

def convert(num): 
   if num == 0:
        return 0
   return (num % 2 + 10 * convert(num // 2)) 


def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

def EvenNums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter an even number")
    elif num == 2:
        return num
    else:
        return EvenNums(num-2)

EvenNums(9)

# NUMBER: 0 1 1 2 3 5 8 13 21
# INDEX:  0 1 2 3 4 5 6 7  8

import time

def fibonacci(idx):
    seq = [0, 1]
    
    for i in range(idx):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx-1) + Fibonacci(idx-2)

print("**** recursion ****")
rec = time.time()
print(Fibonacci(8))
print("speed : " + str(time.time()-rec))

print("**** iteration ****")
it = time.time()
print(fibonacci(8))
print("speed : " + str(time.time()-it))

# * args

"""
    Python allows you to have functions with varying numbers of arguments.
    Using *args as a function parameter enables you to pass an arbitrary
    number of arguments to that function. The arguments are then accessible
    as the tuple in the body of the function.
"""

def function(name_arg, *args):
    print(name_arg)
    print(args)

function(1, 2, 3, 4, 5)

"""
    The parameter *args must come after the named parameters to a function.
    The name args is just a convention; you can choose to use another.
"""

# **kwargs 

"""
    **kwargs(standing for keyword arguments) allows you to handle named
    arguments that you have not defined in advance.

    The keyword arguments return a dictionary in which the keys are 
    argument names, and the values are the argument values.
"""

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

"""
    The arguments returned by **kwargs are not included in *args.
"""