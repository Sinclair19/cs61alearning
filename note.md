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

