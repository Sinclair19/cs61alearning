# 1 

## 1.1 Getting Started

## 1.2 Elements of Programming

### 1.2.1 Expression

### Call Expressions
This call expression has subexpressions: the operator is an expression that precedes parentheses, which enclose a comma-delimited list of operand expressions.  
The order of the arguments in a call expression matters.   
calculating order: first operand, second operand ...

### 1.2.3 Importing Library Functions

### 1.2.4 Names and the Environment
When a name is bound to a new value through assignment, it is no longer bound to any previous value.  

### 1.2.5 Evaluating Nested Expressions
- Evaluate the operator and operand subexpressions, then
- Apply the function that is the value of the operator subexpression to the arguments that are the values of the operand subexpressions.
  
### 1.2.6 The Non-Pure Print Function
- Pure Function
  - just return values
- Non-Pure Function
  - have side effects

- None
  - A function that does not explicitly return a value will return None
  - None is not displayed by the interpreter as the value of an expression

## 1.3 Defining New Functions

### 1.3.1 Environments
- An environment is a swquence of frames
  - The global frame alone
  - A local, then the gloabal frame

### 1.3.2 Calling User-Defined Functions

### 1.3.4 Local Names
- Principle 
  - the meaning of a function should be independent of the parameter names chosen by its author

### 1.3.5 Choosing Names

### 1.3.6 Functions as Abstractions

### 1.3.7 Operators

## 1.4 Designing Functions

### 1.4.1 Documentation
When you call help with the name of a function as an argument, you see its docstring (type q to quit Python help).  

### 1.4.2 Default Argument Values

## 1.5 Control

### 1.5.1 Statements
A statement is executed by the interpreter to perform an action

### 1.5.2 Compound Statements
Each clause is considered in order
- Evaluate the header's expression
- If it is a true value, execute the suite & skip the remaining clauses

Conditional Expression
- `consequent` if `predicate` else `alternative`
  - Evaluate the `predicate` expression
  - It it's a true value, the value of the whole expression is the value of the `consequent`
  - Otherwise, the value of the whole expression is the value of the `alternative`


### 1.5.4 Conditional Statements
- Conditional statements. 
    A conditional statement in Python consists of a series of headers and suites: 
    a required `if` clause, 
    an optional sequence of `elif` clauses, 
    and finally an optional `else` clause
- Boolen contexts
  - False values
    - 0, None, False
  - True values
    - Anything else (True)

logical operators
- `left` `and` `right`
  - Evalutae the subexpression `left`
  - If the result is a false value v, then the expression evaluates to v
  - Otherwise the expression evaluates to the value of the subexpression `right`
- `left` `or` `right`
  - Evaluate the subexpression `left`
  - If the result is a true value v, then the expression evaluates to v
  - Otherwise, the expression evaluates to the value of the subexpression `right`


### 1.5.5 Iteration
In addition to selecting which statements to execute, control statements are used to express repetition. 

### 1.5.6 Testing
`python3 -m doctest <python_source_file>`

## 1.6 Higher-Order Functions
Higher-order function: A function that tekes a function as an argument value or returns a function as a return value  

Functions are first-class: Functions can be manipulated as values in our programming language  

A function's domain is the set of all inputs it might possibly take as arguments  
A function's range is the set of output values it might possibly return  
A pure function's behavior is the relationship it creats between input and output  

### 1.6.1 Functions as Arguments
Using an identity function that returns its argument, we can also sum natural numbers using exactly the same summation function.  
The summation function can also be called directly, without definining another function for a specific sequence.  

### 1.6.2 Functions as General Methods
`assert condition, 'AssertionError'`
The assert keyword is used when debugging code.
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

### 1.6.3 Defining Functions III: Nested Definitions
call expression as operator expressions  
Function defined within other function bodies are bound to names in a local frame  

### 1.6.4 Functions as Returned Values
An important feature of lexically scoped programming languages is that locally defined functions maintain their parent environment when they are returned.  

Every user-definded function has a parent frame (often global)  
The parent of a function is the frame in which it was defined  
Every local frame has a parent frame (ofent global)  
The parent of a frame is the parent of the function called  

- Draw an Environment Diagram
  - When a funtcion is defined
    - Create a function value : `func <name>(<formal parameters>) [parent=<parent>]`
    - Bind `<name>` to the function value in the current frame
  - When a function is called
    - Add a local frame, titled with the `<name>` of the function being called
    - Copy the parent of the function to the local frame: `[parent=<label>]`
    - Bind the `<formal parameters>` to the arguments in the local frame
    - Execute the body of the function in the environment that starts with the local frame

```py
def print_sums(n):
  '''
  a funtcion that add and print with a loop
  >>> print_sums(1)(3)(5)
  1
  4
  9
  '''
  print(n)
  def next_sum(k):
    return print_sums(n+k)
  return next_sum
```

### 1.6.6 Currying
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument.  
More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y).

```py
def curry2(f):
  '''
  equal to curry2 = lambda f: lambda x: lambda y: f(x, y)
  >>> from operator import add
  >>> m = curry2(add)
  >>> add_three = m(3)
  >>> add_three(2)
  5
  >>> add_three(2019)
  2023
  '''
  def g(x):
    def h(y):
      return f(x,y)
    return h
  return g
```

### 1.6.7 Lambda Expressions
lambda  
`lambad x: k` 
`x input` 
`k return value`  

differs to def:
  Only teh def statement gives the function an intrinsic name  

### 1.6.8 Abstractions and First-Class Functions
- The right of First-class elements 
  - They may be bound to names.
  - They may be passed as arguments to functions.
  - They may be returned as the results of functions.
  - They may be included in data structures.

Python awards functions full first-class status, and the resulting gain in expressive power is enormous.  

Function Abstractions
Naming tips
- Names can be long if they help document your code
- Names can be short if they represent generic quantities: couts, arbitrary functions, arguments to mathematical operations,etc
  - n, k, i usually integers
  - x, y, z usually real numbers
  - f, g, h usually functions

### 1.6.9 Function Decorators
Python provides special syntax to apply higher-order functions as part of executing a def statement, called a decorator.  

`from ucb import trace`
`@trace`

```py
@trace1  #Function decorator
def triple(x): # Decorated function
  return 3 * x
```
equal to
```py
def triple(x):
  return 3 * x
triple = trace1(triple)
```

## 1.7 Recursive Functions
A function is called recursive if the body of the function calls the function itself, either directly or indirectly. 

Recursion in Environment Diagrams
- The same function fact is called multiple times
- Different frames keep track of the different arguments in each call
- What n evaluates to depends upon which is the current environment
- Each call to fact solves a simpler problem than the last: samller n

The Luhn Algorithm: check digit

### 1.7.1 The Anatomy of Recursive Functions

The Anatomy of a Recursive Function
- The def statment header is similar to other functions
- Conditional statments check for base cases
- Base cases are evaluated without recursive calls
- Recursive cases are evaluated with recursive calls

### 1.7.2 Mutual Recursion
When a recursive procedure is divided among two functions that call each other, the functions are said to be mutually recursive.  

Mutually recursive functions can be turned into a single recursive function by breaking the abstraction boundary between the two functions.

### 1.7.3 Printing in Recursive Functions
```py
def cascade(n):
  '''print num in order
  >>> cascade(123)
  123
  12
  1
  12
  123
  '''
  if n < 10:
    print(n)
  else:
    print(n)
    cascade(n // 10)
    print(n)
```  
- Each cascade frame is from a different call to cascade  
- Until the Return value appears, that call has not completed  
- Any statement can appear before or after the recursive call  

### 1.7.4 Tree Recursion
Another common pattern of computation is called tree recursion, in which a function calls itself more than once.   

fib number
```py
dicfib = {0:0,1:1}
def fib(n):
    if n in dicfib.keys():
        return dicfib[n]
    else:
        dicfib[n] = fib(n-2) + fib(n-1)
        return dicfib[n]
def fib2(n):
    ''' tradition way '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-2) + fib2(n-1)
```

### 1.7.5 Example: Partitions
The number of partitions of a positive integer n, using parts up to size m, is the number of ways in which n can be expressed as the sum of positive integer parts up to m in increasing order.  

Counting Partitions
```py
def count_partitions(n, m):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  elif m == 0:
    return 0
  else:
    with_m = count_partitions(n-m, m)
    without_m = count_parations(n, m-1)
    return with_m + without_m
```

# 2 Building Abstractions with Data

## 2.1 Introduction

### 2.1.1 Native Data Types
int, float, bool etc

## 2.2 Data Abstraction
Date abstractionL: A methodology by which functions enforce  an abstraction barrier between representation and use

### 2.2.1 Example: Rational Numbers
A rational number is a ratio of integers, and rational numbers constitute an important sub-class of real numbers.   
- rational(n, d) returns the rational number with numerator n and denominator d.
- numer(x) returns the numerator of the rational number x.
- denom(x) returns the denominator of the rational number x.

### 2.2.2 Pairs
Two-element lists are not the only method of representing pairs in Python.  
Any way of bundling two values together into one can be considered a pair.  
Lists are a common method to do so.

```py
from operator import getitem
getitem(pair, 0)
```

### 2.2.3 Abstraction Barriers
For rational numbers, different parts of the program manipulate rational numbers using different operations, as described in this table.  


|Parts of the program that...|Treat rationals as...	|	Using only...|
|----|----|----|
|Use rational numbers to perform computation|whole data values|add_rational, mul_rational, rationals_are_equal, print_rational|
|Create rationals or implement rational operations|numerators and denominators|rational, numer, denom|
|Implement selectors and constructor for rationals|two-element lists|list literals and element selection|

### 2.2.4 The Properties of Data

## 2.3 Sequences
A sequence is an ordered collection of values.  
Sequences' common bahavior  
- Length. A sequence has a finite length. An empty sequence has length 0.
- Element selection. A sequence has an element corresponding to any non-negative integer index less than its length, starting at 0 for the first element.

### 2.3.1 Lists
A list value is a sequence that can have arbitrary length.   

### 2.3.2 Sequence Iteration
A for statement consists of a single clause with the form:  

for `<name>` in `<expression>`:
    `<suite>`

A for statement is executed by the following procedure:  
- Evaluate the header `<expression>`, which must yield an iterable value.
- For each element value in that iterable value, in order:
  - Bind `<name>` to that value in the current frame.
  - Execute the `<suite>`.

- Sequence unpacking:  
A common pattern in programs is to have a sequence of elements that are themselves sequences, but all of a fixed length.   

### 2.3.3 Sequence Processing
- List Comprehensions
- Aggregation
  - A third common pattern in sequence processing is to aggregate all values in a sequence into a single value. The built-in functions sum, min, and max are all examples of aggregation functions.  
- Higher-Order Functions
  - The common patterns we have observed in sequence processing can be expressed using higher-order functions.
- Conventional Names

### 2.3.4 Sequence Abstraction
- Membership. 
  - A value can be tested for membership in a sequence. Python has two operators in and not in that evaluate to True or False depending on whether an element appears in a sequence.
- Slicing
  - Sequences contain smaller sequences within them. 
  - Slicing creates new values

Sequence Aggregation
- `sum(iterable[, start])` -> value
  - reutrn the sum of an iterable of numbers (Not strings) plus the value of parameter 'start' (which is defults to 0). When the iterable is empty, return start
- `max(iterable[, key = func])` -> value  `max(a, b, c, ...[, key = func])` -> value
  - with a singel iterable argument, return its largest item. With two or more arguments, return the largest argument
- `all(iterable)` -> bool
  - return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True

### 2.3.5 Strings
- representing data
- representing language
- representing programs:
  - exec('')

- Membership
- Multiline Literals (''')
- String Coercion
- Further reading

Dictionary
- Dictionary keys have two restrictions
  - A key of a dictionary cannot be a list or a dictionary (or any mutable type)
  - Two keys cannot be equal; There can be at most one value for a given key


### 2.3.6 Trees
Nesting lists within lists can introduce complexity. The tree is a fundamental data abstraction that imposes regularity on how hierarchical values are structured and manipulated.  

A tree has a root label and a sequence of branches.  
Each branch of a tree is a tree.  
A tree with no branches is called a leaf.  
Any tree contained within a tree is called a sub-tree of that tree (such as a branch of a branch).  
The root of each sub-tree of a tree is called a node in that tree.

The data abstraction for a tree consists of the constructor `tree` and the selectors `label` and `branches`. We begin with a simplified version.

```py
def tree(root_label, branches=[]):
    for branch in branches:
      assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]
```
The `is_tree` function is applied in the tree constructor to verify that all branches are well-formed.  
```py
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
```

The `is_leaf` function checks whether or not a tree has branches.  

```py
def is_leaf(tree):
    return not branches(tree)
```

Tree-recursive functions are also used to process trees. For example, the count_leaves function counts the leaves of a tree.  

```py
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
```

Trees can also be used to represent the partitions of an integer. A partition tree for n using parts up to size m is a binary (two branch) tree that represents the choices taken during computation.  

```py
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])
```

### 2.3.7 Linked Lists
A linked list is a pair containing the first element of the sequence and the rest of the sequence.  
The second element is also a linked list. The rest of the inner-most linked list containing is 'empty', a value that represents an empty linked list.  

```py
empty = 'empty'
def is_link(s):
    return s == empty or (len(s) ==2 and is_link(s[1]))

def link(first, rest):
    assert is_link(rest), "rest must be a linked list"
    return [first, rest]

def first(s):
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element"
    return s[0]

def rest(s):
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no rest"
    return s[1]
```

```py
def len_link(s):
    """Return the length of a linked list s."""
    length = 0
    while s != empty:
      s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
      s, i = rest(s), i - 1
    return first(s)
```
This function can be easily turn into recursive function

```py
def extend_link(s, t)
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
```


## extend knowledge
- Binary Numbers
  - n-bit unsigned binary numbers: 0 - 2**n -1
  - n-bit signed binary numbers : -2**(n-1) - 2**(n-1)-1
- Designing Circuits
  - build truth-table for all possible input/output values
  - build sub-expressions with and/not for each output column
  - combine two at a time, sub-expressions with an or
  - draw circuit diagram

## 2.4 Mutable Data

### 2.4.1 The Object Metaphor
Objects
- Objects represent information
- They consist of data and behavior, bundled together to create abstractions
- Obejcts can represent things, but also properties, interactions, & processes
- A type fo object is called a calss; calsses are first-class values in Python
- Object-oriented programming:
  - A metaphor for organizing large programs
  - Special syntax that can improve the composition of programs
- In Python, every value is an object
  - All objects have attributes
  - A lot of data manipulation happens through object methods
  - Functions do one thing; objects do many related things

### 2.4.2 Sequence Objects
- Some objects can change
  - All names that refer to the same object are affected by a mutation
  - Only objects of mutable types can change: lists & dictionaries

- Identity Operators
  - Identity
    - `<exp0>` is `<exp1>`
    - evaluates to `True` if both `<exp0>` and `<exp1>` evaluate to the same object
  - Equality
    - `<exp0>` == `<exp1>`
    - evaluates to `True` if both `<exp0>` and `<exp1>` evaluate to equal values
  - Idnetical objects are always equal values

- List comprehensions
A list comprehension always creates a new list.  

- Tuples  
  - Tuples are immutable sequences
    - Immutable values are protected from mutation
    - The value of an expression can change because of changes inanames or objects
    - An immutable sequence may still change if it contains a mutable value as an element

Mutable Default Arguments are Dangerous  
A default argument value is part of a function value, not generated by a call  

### 2.4.3 Dictionaries
The dictionary type also supports various methods of iterating over the contents of the dictionary as a whole. The methods `keys`, `values`, and `items` all return iterable values.  
A list of key-value pairs can be converted into a dictionary by calling the dict constructor function.  
- Dictionaries do have some restrictions:
  - A key of a dictionary cannot be or contain a mutable value.
  - There can be at most one value for a given key.

### 2.4.4 Local State
Lists and dictionaries have local state: they are changing values that have some particular contents at any point in the execution of a program. The word "state" implies an evolving process in which that state may change.  

Execution rule for assignment statements
- Evaluate all expressions right of =, from left to right
- Bind the names on the left to the resulting values in the current frame  

Non local assignment & persistent local state  
`nonlocal <name>`  

Effect: Future assignments to that name change its pre-existing binding in the first non-local frame of the current environment in which that name is bond  

Form the Python 3 language reference
- Names listed in nonlocal statement must refer to pre-existing bingdings in an enclosing scope.
- Names listed in a nonlocal statement must not collide with pre-existing bingdings in the local scope

### 2.4.5 The Benefits of Non-Local Assignment
In particular, non-local assignment has given us the ability to maintain some state that is local to a function, but evolves over successive calls to that function.   

### 2.4.6 The Cost of Non-Local Assignment
**Sameness and change**. These subtleties arise because, by introducing non-pure functions that change the non-local environment, we have changed the nature of expressions.  
An expression that contains only pure function calls is `referentially transparent`; its value does not change if we substitute one of its subexpression with the value of that subexpression.  

Referential Transparency, Lost
- Expressions are referentially transparent if substituting an expression with its value does not change the meaning of a program
- Mutation operations violate the condition of referentail transparency because they do more than just return a value; they change the environment

### 2.4.7 Implementing Lists and Dictionaries

Mutable Values & Persistent Local State
Mutable values can be changed without a nonlocal statement

### 2.4.8 Dispatch Dictionaries

### 2.4.9 Propagating Constraints
Mutable data allows us to simulate systems with change, but also allows us to build new kinds of abstractions.  

## 4.2 Implicit Sequences

### 4.2.1 Iterators
A container can provide an iterator that provides access to its elements in some order  

`iter(iterable)`: Return an iterator over the elements of an iterable value  

`next(iterator)`: Return the next element in an iterator

### 4.2.2 Iterables
Any value that can produce iterators is called an iterable value.  

Dictionary iterator
A dictionary, its keys, its values, and its items are all iterable values  
- The order of items in a dictionary is the order in which they were added
- Historically, items appeared in an arbitrary order (Python 3.5 and earlier)

### 4.2.3 Built-in Iterators

Built-in Functions for iteration  
- Many built-in Python sequence operations return iterators that compute results lazily  
`map(func, iterable)`: Iterate over func(x) for x in iterable  
`filter(func, iterable)`: Iterate over x in iterable if func(x)  
`zip(first_iter, second_iter)`: Iterate over co-indexed (x, y ) pairs  
`reversed(sequence)`: Iterate over x in a sequence in reverse order 

- To view the contents of an iterator, place the resulting elements into a container  
`list(iterable)`: Create a list containing all x in iterable  
`tuple(iterable)`: Create a tuple containing all x in iterable  
`sorted(iterable)`: Create a sorted list containing all x in iterable  

### 4.2.4 For Statements
After iter reach end, the iter cann't be used to track form start to end

### 4.2.5 Generators and Yield Statements

Generators  
- A generator function is a function that yields values instead of returning them  
- A normal function returns once; a generator function can yield multiple times  
- A generator is an iterator created automatically by calling a generator function  
- When a generator function is called, it returns a generator that iterates over its yields  

### 4.2.6 Iterable Interface

### 4.2.7 Creating Iterables with Yield
Generators & Iterators  
- A yield form statement yields all values from an iterator or iterable

### 4.2.8 Iterator Interface

## 2.5 Object-Oriented Programming

### 2.5.1 Objects and Classes
A class combines and abstracts data and functions  
An object is an instantiation of a class  

A method for organizing modular programs  
- Abstraction barriers
- Bundling together information and related behavior
  
A metaphor for computation using distributed state  
- Each object has its own local state
- Each object also knows how to manage its own local state, based on method calls
- Method calls are messages passed between objects
- Several objects may all be instances of a common type
- Different types may relate to each other

### 2.5.2 Defining Classes

The Class Statement  
```python
class <name>:
    <suite>
```

Object Construction  

When a class is called:
- A new instance of that class is created
- The `__init__` method of the class is called with the new object as its first argument (named self), along with any additional arguments provided in the call expression


Methods

Dot Expressions
- Objects receive messages via dot notation
- Dot notation accesses attributes of the instance or its class

### 2.5.3 Message Passing and Dot Expressions

Objects also have named local state values (the instance attributes), but that state can be accessed and manipulated using dot notation, without having to employ nonlocal statements in the implementation.  

`<expression> . <name>`  
To evaluate a dot expression:
- Evaluate the `<expression>` to the left of the dot, which yields the object of the dot expression.  
- `<name>` is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned  
- if not, `<name>` is looked up in the class, which yields a class attribute value  
- That value is returned unless it is a function, in which case a bound method is returned instead  

All objects have attributes, which are name-value pairs  
Classes are objects too, so they have attributes  
Instance attribute: attribute of an instance  
Class attribute: attribute of the class of an instance  

#### Python object system:
- Functions are objects  
- Bount mothods are also objects: a function that has its first parameter "self" alreday bound to an instance  
- Dot expressions evaluate to bound methods for class attributes that are functions  
`<instance>.<method_name>`

### 2.5.4 Class Attributes
Some attribute values are shared across all objects of a given class. Such attributes are associated with the class itself, rather than any individual instance of the class.


#### Looking Up Attributes by Name
To evaluate a dot expression:
- Evaluate the `expression` to the left of the dot, which yields the object of the dot expression
- `name` is matched against the instance attributes of that object; If an attribute with that name exists, its value is returned
- If not, `name` is looked up in the calss, which  yields a class attribute value
- That value is returned unless it is a function, in which case a bound method is returned instead


#### Assignment to Attributes
Assignment statements with a dot expression on their left-hand side affect attributes for the object fo that dot expression
- If the object is an instance, then assignment sets an instance attribute
- If the object is a class, then assignment sets a class attribute

### 2.5.5 Inheritance

#### Inheritance
- Inheritance is a method for relating classes together  
- A common use: Two similar classes differ in their degree of specialization 
- The specialized class may have the same attributes as the general class, along with some special-case behavior  

#### Inheritance and Composition
- Inheritance is best for representing is-a relationships  
- Composition is best for representing has-a relationships  

### 2.5.6   Using Inheritance

```py
class <name>(<base class>):
    <suite>
```

- Conceptlually, the new subclass "shares" attributes with its base class
- The subclass may override certain inherited attributes  
- Using inheritance, we implement a subclass by specifying its differences from the base class  

Looking Up Attribute Names on Classes
- If it names an attribute in the class, return the attribute value
- Otherwise, look up the name in the base class, if there is one

### 2.5.8 The Role of Objects

Object-Oriented Design
Designing for Inheritance
- Don't repeat yourself; use existing implementations
- Attributes that have been overridden are still accessible via class objects
- Look up attributes on instances whenever possible

## 2.7 Object Abstraction

### 2.7.1 String Conversion
String Representations
In python, all objects produce two string representations:
- The `str` is legible to humans
- The `repr` is legible to the Python interpreter

The `str` and `repr` strings are often the same, but not always

The `repr` function returns a Python expression (a string) that evaluates to an equal object

The result of calling `str` on the value of an expression is what Python prints using `print` function

Polymorphic Functions
A function that applies to many (poly) different forms (morph) of data
`str` and `repr` are both polymorphic; they apply to any object
`repr` invokes a zero-argument method `__repr__` on its argument
`str` invokes a zero-argument method `__str__` on its argument

### 2.7.2 Special Methods

Special Method Names in Python
Ceratin names are special because they have built-in behavior  
These names always start and end with two underscores  

### 2.7.3 Multiple Representations

Interfaces
- Message passing: Objects interact by looking up attributes on each other (passing messages)
  - The attribute look-up rules allow different data types to respond to the same message
- A sharde message (attribute name) that elicits similar behavior from different object classes is a powerful method of abstraction
  - A interfaces is a set of shared messages, along with a specification of what they mean 

Properties. 
The requirement that two or more attribute values maintain a fixed relationship with each other is a new problem.   
One solution is to store attribute values for only one representation and compute the other representation whenever it is needed.  
Python has a simple feature for computing attributes on the fly from zero-argument functions.   
The `@property` decorator allows functions to be called without call expression syntax (parentheses following an expression).   


### 2.7.4 Generic Functions
Type dispatching. One way to implement cross-type operations is to select behavior based on the types of the arguments to a function or method.   
The built-in function `isinstance` takes an object and a class. It returns true if the object has a class that either is or inherits from the given class.

## 2.8 Efficiency

### 2.8.1 Measuring Efficiency
```python
def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted
```
```python
def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted
```
  
### 2.8.2 Memoization
```python
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
```

### 2.8.3 Orders of Growth

Quadratic Time
Functions that process all pairs of values in a sequence of length n take quadratic time  

### 2.8.5 Growth Categories

Common Orders of Growth
- Exponential growth
  - recursive fib
  - Incrementing n multiplies time by a constant
- Quadratic growth
  - overlap
  - Incrementing n increases time by n times a constant
- Linear growth
  - slow exp
  - Incrementing n increases time by a constant
- Logarithmic growth
  - exp_fast
  - Doubling n only increments time by a constant
- Constant growth
  - Increasing n doesn't affect time

Order of Growth Notation

The consumption of Space
Active environments:
- Environments for any function calls currently being evaluated
- Parent environments of functions named in active environments

## 2.9 Recursive Objects

### 2.9.1 Linked List Class
Linked Lists
A linked list is either empty or a first value and the rest of the linked list  
The empty list is a special case of a linked list that has no first element or rest   


- Linked List Processing
Range, Map, and Filter for Linked Lists

Recursive Construction  
We follow the same recursive analysis of the problem as we did while counting: partitioning n using integers up to m involves either  

- partitioning `n-m` using integers up to `m`, or
- partitioning `n` using integers up to `m-1`.

For base cases, we find that 0 has an empty partition, while partitioning a negative integer or using parts smaller than 1 is impossible.  

Linked Lists Mutation

### 2.9.2 Tree Class
Trees can also be represented by instances of user-defined classes, rather than nested instances of built-in sequence types. A tree is any data structure that has as an attribute a sequence of branches that are also trees.

### 2.9.3 Sets
In addition to the list, tuple, and dictionary, Python has a fourth built-in container type called a set  
Set literals follow the mathematical notation of elements enclosed in braces  Duplicate elements are removed upon construction  

one more built-in Python container type
- Set literals are enclosed in braces
- Duplicate elements are removed on construction
- Sets have arbitrary order

## extend knowledge

Modular Design
Separation of Concerns
A design principle: Isolate different parts of a program that address different concerns  
A modular component canbe developed and tested independently  

Linear-Time intersection of Sorted Lists

Given two `sorted` lists with no repeats, return the number of elements that appear in both  

```python
def fast_overlap(s, t):
    '''return the overlap between sorted S and sorted T.
    '''
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
          count, i, j = count + 1, i+1, j+1
        elif s[i] < t[j]:
          i = i + 1
        else:
          j = j + 1
        return count
```

Land Owners
Instance attributes are found before class attributes  
class attributes are inherited

# 3 Interpreting Computer Programs

## 3.1 Introduction

### 3.1.1 Programming Languages
Scheme

## 3.2 Functional Programming

### 3.2.1 Expressions
Scheme Fundamentals
expressions
- Primitive expressions
- Cominations

Numbers are self-evaluating: symbols are bound to values
Call expressions include an operator and `0` or more operands in parentheses

### 3.2.2 Definitions

Special Forms
A combination that is not a call expression is a special form
- If expression: `(if <predicate> <consequent> <alternative>)`
- And and or: `(and <e1> <e2> ...)` `(or <e1> <e2>)`
- Bingding symbols `(define <symblo> <expression>)`
- New procedures `(define (<symbol> <formal parameters>) <body>)`

Lambda Expressions
(lambda (`<formal-parameters>`) `<body>`)

### 3.2.3 Compound values
Pairs are built into the Scheme language. For historical reasons, pairs are created with the `cons` built-in function, and the elements of a pair are accessed with `car` and `cdr`

### 3.2.4 Symbolic Data
All the compound data objects we have used so far were constructed ultimately from numbers. One of Scheme's strengths is working with arbitrary symbols as data.

### 3.2.5 Turtle graphics
The implementation of Scheme that serves as a companion to this text includes Turtle graphics, an illustrating environment developed as part of the Logo language (another Lisp dialect).  
This turtle begins in the center of a canvas, moves and turns based on procedures, and draws lines behind it as it moves.

## Scheme knowledge
Cond & Begin
The cond special form that behaves like if-elif-else statements in Python  
The begin special form combines multiple expressions into one expression  

Let Expressions
The let special form binds symbols to values temporarily just for one expression

Lists
- cons: Two-argument procedure that creates a linked list
- car: Procedure that returns the first element of a list
- cdr: Procedure that returns the rest of a list
- nil: The empty list

Quotation is used to refer to symbols directly in Lisp

A Scheme Expression is a Scheme List
Scheme programs consist of expressions, which can be:
- Primitive expressions
- Combinations

The build-in Scheme list data structure (which is a linked list) can represent combinations

Quasiquotation
There are two ways to quote an expression
- quote `'(a b) => (a b)`
- quasiquote ``(a,b) => (a b)`
different because parts of a quasiquoted expression canbe unquoted with `,`
- quote `'(a ,(+ b 1)) => (a (unquote (+ b 1)))`
- quasiquote ``(a ,(+ b 1)) => (a 5)`

Quasiquotation is particularly convenient for generating Scheme expressions


## 3.3 Exceptions
- Exceptions
Unhandled exceptions will cause Python to halt execution and print a stack trace  
Exceptions are objects. They have classes with constructors
They enable non-local continuations of control

- Assert Statements
Assert statements raise an exception of type AssertionError
`assert <exression>, <string>`  
Assertions are designed to be used liberally.  
They can be ignored to increase efficiency by running Python with the "-O" flag. "O" stans for optimized  
Whether assertions are enabled is governed by a bool `__debug__`  

- Raise Statements  
Exceptions are raised with a raise statement
`raise <expression>`
built in error type  
`TypeError` 
`NameError`
`keyError`
`RuntimeError`

- Try Statements
Try statements handle exceptions
```py
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
```
Execution rule:
- The `<try suite>` is executed first
- If, during the course of executing the `<try suite>`, an exception is raised that is not handled otherwise,  and If the class of the exception inherits from `<exception class>`,  then the `<except suite>` is executed, with `<name>` bound to the exception  

### 3.3.1 Exception Objects
Exception objects themselves can have attributes, such as the error message stated in an assert statement and information about where in the course of execution the exception was raised.  


## 3.4 Interpreters for Languages with Combination

Programming Languages
A computer typically executes programs written in many different programming languages
Machine languages: statements are interpreted by the hardware itself
- aA fixed set of instructions invoke operations implemented by the circuitry of the central processing unit
- Operations refer to specific hardware memory addresses; no abstarction mechanisms

High-level languages: statements & expressions are interpreted by another program or complied(translated) into another language
- Provide means of abstracion such as naming, function definition, and objects
- Abstract away system datails to be independent of hardware and operating system

A programming languages has:
- Syntax: The legal statements and expressions in the language
- Semantics: The execution/evaluation rule for those statements and expressions

To create a new programming language, you either need a:
- Specification: A document describe the precise syntax and semantics of the language
- Canonical Implementation: An interpreter or complier for the language

### 3.4.1 A Scheme-Syntax Calculator

### 3.4.2 Expression Trees
Calculator  
The Pair class  
The Pair class represents Scheme pairs and lists. A list is a pair whose second element is either a list or nil.

Handling Exceptions
An interactive interpreter prints information about each error  
A well-designed interactive interpreter should not halt completely on an error, so that the user has an opportunity to try again in the current environment

### 3.4.3 Parsing Expressions
Parsing is the process of generating expression trees from raw text input  
- Lexical analysis
- Syntactic analysis

Parsing
A parser takes text and returns an expression

Recursive Syntactic Analysis
A predictive recursive descent parse inspects only k tokens to decide how to proceed

Syntactivc Analysis
Syntactic analysis indentifies the hierarchical structure of an expression, which may be nested  
Each call to scheme_read consumes the input tokens for exactly one expression  

- Base case: symbols and numbers
- Recursive call: scheme_read sub-expressions and combine them

### 3.4.4 Calculator Evaluation
The scalc module implements an evaluator for the Calculator language. The calc_eval function takes an expression as an argument and returns its value  
```py
def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return simplify(exp)
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return simplify(calc_apply(exp.first, arguments))
    else:
        raise TypeError(exp + ' is not a number or call expression')
```
```py
def calc_apply(operator, args):
    """Apply the named operator to a list of args."""
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + ' is an unknown operator')
```

- Read-eval-print loops
```py
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(calc_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return
```

## 3.5 Interpreters for Languages with Abstraction

### 3.5.1 Structure
Interpreters  

The Structure of an Interpreter
- Eval (requires an environment for symbol lookup)
  - Base cases
    - Primitive values (numbers)
    - Look up values bound to symbols
  - Recursive calls
    - Eval(operator, operands) of call expressions
    - Apply(procedure, arguments)
    - Eval(sub-expressions) of specail forms
- Apply (Creates a new environment each time a user-defined procedure is applied)
  - Base cases
    - Built-in primitive procedures
  - Recursive calls
    - Eval(body) of user-defined procedures

Scheme Evaluation  
The scheme_eval function dispatches on expression form:
- Symbols are bound to values in the current environment
- Self-evaluating expressions are returned
- All other legal expressions are represented as Scheme lists, called combinations

Logical Special Forms  
Logical forms may only evaluate some sub-expressions  

Quotation  
The quote special form evaluates to the quoted expression, which is not evaluated  

### 3.5.2 Environments
Applying User-Defined Procedures  

To apply a user defined rocedure, create a new frame in which formal parameters are bound to argument values, whose parent is the enve of the procedure  
Evaluate the body of the procedure in the environment that starts with this new frame  

### 3.5.3 Data as Programs

## 4.3 Declarative Programming
Database Management Systems  

A table is a collection of records, which are rows that have a value for each column  

Declarative Programming  

In declarative languages such as SQL & Prolog:
- A "program" is description of the desired result
- The interpreter figures out how to generate the result

In imperative languages such as Python & Scheme:
- A "program" is a description of computational processes
- The interpreter carries out execution/evaluation rules

SQL overvies  

The SQL language is an ANSI and ISO standard, but DBMS's implement custom variants  
- A select statement a new table, either from scratch or by projecting a table
- A create table statment gives a global name to a table
- Lots of other statements exist: analyze, delete, explain, insert, replace, update, etc
- Most of the important action is in the select statement
- The code for executing select statements fits on a single sheed of paper(next lecture)

### 4.3.1 Tables
The SQL language is standardized, but most database systems implement some custom variant of the language that is endowed with proprietary features  

### 4.3.2 Select Statements

- Selecting Value Literals  

  A `select` statement always includes a comma-separated list of column descriptions  

  A column description is an expresson, optionally followed by `as` and a column name  

`select [expression] as [name], [expression] as [name];`  

Selecting literals creates a one-row table  

The union of two select statments is a table containing the rows of both of their results  

SQL is often used as an interactive language  

The result of a `select` statement is displayed to the user, but not stored  

A `create table` statement gives the result a name  

`create table [name] as [select stament];`
 
- Select Statements Project Existing Tables  

  A `select` statement can specify an input table using a `from` clause  
  A subset of the rows of the input table can be selected using a where clause  
  An ordering over thhe remaining rows can be declared using an `order by` clause  
  Column descriptions determine how each input row is projected to a result row   

- Arithmetic in Select Expressions  
  In a select expression, column names evaluate to row values  
  Arithmetic expressions can combine row values and constants

### 4.3.3 Joins

Joining Tables

**Joining Two Tables**  
Two tables A&B are joined by a comma to yield all combos of a row from A & a row from B  


**Joining a Table with Itself**  

Aliases and Dot Expression  

Two tables may share a column name; dot expressions and aliases disambiguate column values  

`select [columns] from [table] where [condition] order by [order]`
`[table]` us a cinna-sparated list of table names with optional aliases  

**Joining Multiple Tables**

Multiple tables can be joined to yield all combinations of rows from each  

**Numerical Expressions**  

Expressions can contain function calls and arithmetic operators  
`select [columns] from [table] where [expression] order by [expression];`  

`[columns]`: `[expression] as [name], [expression] as [name]`    

Combine values: `+`, `-`, `*`, `/`, `%`, `and`, `or`  
Transform values: `abs`, `round`, `not`, `-`  
Compare values: `<`, `<=`, `>`, `>=`, `<>`, `!=`, `=`  

**String Expressions**  
`||` combine two string together  

### 4.3.4 Interpreting SQL

### 4.3.5 Recursive Select Statements

### 4.3.6 Aggregation and Grouping
Multiple aggregate functions can be applied to the same set of rows by defining more than one column. Only columns that are included by the where clause are considered in the aggreagation.  

**Aggregate Functions**  
An aggregate function in the `[columns]` clause computes a value from a group of rows  

`distinct [columns]` means the unique one in columns  

**Mixing Aggregate Functions and Single Values**  
An aggregate function alson selects a row in the table, which may be meaningful  

**Groups**  
Grouping Rows  
Rows in a table can be grouped, and aggregation is performed on each group  
 
`select [columns] from [table] group by [expression] habing [expression];`  

The number of groups is the number of unique values of an expression  
A having clause filters the set of groups that are aggregated  

### More SQL 

**Create Table**

**Drop Table**

**Modifying Table**  
- Insert  
To inset into one column:  
  `INSERT INTO t(column) VALUES (value);`
TO inset into both columns:  
  `INSERT INTO t VALUES (value0, value1);`

- Update  
`UPDATE t SET columnt WHERE;`

- Delete  
`DELETE FROM t WHERE ;`

SQL Injection Attack  
`executescript(cmd)` may cause problem if the command was changed by someone  
use `excute("(?)",[])` to prevent this happen  

Database Connections  


## Extension
### Tail Recursion

Functional Programming
All functions are pure functions  
No re-assignment and no mutable data types  
Name-value bingdings are permanent  
Advantages of functional programming:  
- The value of an expression is independent of the order in which sub-expressions are evaluated
- sub-expressions can safely be evaluated in parallel or on demand (lazily)
- Referential transparency: The value of an expression does not change when we substitute one of its subexpression with the value of that subexpression

### Tail Calls  
A procedure call that has not yet returned is active.  
Some procedure calls are tail calls  
A Scheme interpreter should support an unbounded number of active tail calls using only a constant of space  
A tail call is a call expression in a tail context:
- The last body sub-expression in a lambda expression
- Sub-expressions 2 & 3 in a tail context if expression
- All non-predicate sub-expression in a tail context `cond`
- The last sub-expression in a tail context `and` or `or`
- The last sub-expression in a tail context `begin`

Eval with Tail Call Optimization  
The return value of the tail call is the return value of the current procedure call  
Therefore, tail calls shouldn't increase the environment size  

### Map and reduce  
#### Reduce  

```scheme
(define (reduce procedure s start)
    (if (null? s) start
        (reduce procedure (cdr s) (procedure start (car s)))))
```

Recursive call is a tail call  
Other calls are not; constant space depends on wether `procedure` requires constan space  

#### Map  
- normal way 
```scheme
(define (map procedure s)
        (if (null? s) nil
            (cons (procedre (car s) (map procedure (cdr s))))))
```
- tail recursive way  
```scheme
(define (map procedure s)
        (define (map-reverse s m)
                (if (null? s) m 
                    (map-reverse (cdr s)
                                 (cons (procedure (car s)) m))))
        (reverse (map-reverse s nil)))

(define (reverse s)
        (define (reverse-iter s r)
                (if (null? s) r
                    (reverse-iter (cdr s)
                                  (cons (car s) r))))
        (reverse-iter s nil))
```
### Macros
Macros Perform Code Transformations  
A macro is an operation performed on the source code of a program before evaluation  
Macros exist in mnay languages, but are easiest to define correctly in a language like Lisp  
Scheme has a define-macro special from that defines a source code transformation  

Evaluation procedure of a macro call expression:
- Evaluate the operator sub-expression, which evaluates to a macro
- Call the macro procedure on the operand expressions without evaluating them first  
- Evaluate the expression returned from the macro procedure

