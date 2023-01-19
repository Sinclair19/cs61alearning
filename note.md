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