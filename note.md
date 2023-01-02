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

### 1.5.5 Iteration
In addition to selecting which statements to execute, control statements are used to express repetition. 

### 1.5.6 Testing
`python3 -m doctest <python_source_file>`