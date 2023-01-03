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

### 1.6.6 Currying
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument.  
More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y).

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

### 1.6.9 Function Decorators
Python provides special syntax to apply higher-order functions as part of executing a def statement, called a decorator.  


