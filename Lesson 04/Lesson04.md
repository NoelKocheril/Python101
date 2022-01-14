# Lesson 04 - Functions

A function within python is a block of code which will only run when it is called.

These functions can take data, transform data, and pass back data as defined.

## Creating a Function

Within Python, a function is created by using the `def` keyword. For example:

```
def my_func():
    print("Hello, World!")
```

## Calling a Function

In order to a call a function, we use the function name followed by parenthesis. For example:

```
def my_func():
    print("Hello, World!")

my_func()
```

## Arguments / Parameters

Information can be passed into a function using arguments (also known as parameters).

Arguments are specified after the function name, inside the parentheses. A given function can have as many arguments as you want, they just need to be separated by commas.

The following name has a single argument `fname`, which when we call the function we must provide the value we would like to use with it:

```
def my_func(fname):
    print(f"Hello {fname}!!!")

my_func("Noel")
my_func("Vit")
my_func("Steve")
```

### Number of Arguments

By default, a function must be called with the same number of arguments it was defined with. This entails that a function that expects two arguments will need to be called with two arguments, not more, and not less. For example:

#### Valid Example

```
def my_func(fname, lname):
    print(f"Hello {fname} {lname}!!!")

my_func("Noel", "Kocheril")
```

#### Invalid Example

```
def my_func(fname, lname):
    print(f"Hello {fname} {lname}!!!")

my_func("Arjun")
```

### Keyword Arguments

When calling a function with multiple arguments, we can choose to ignore the order of arguments by naming the arguments ourselves. This is done by using the `key = value` syntax. For example:

```
def my_func(child3, child2, child1):
    print(f"The youngest child is {child3}")

my_func(child1 = "Steve", child2 = "Bob", child3 = "Jim")   # The youngest child is Jim
my_func("Steve", "Bob", "Jim")                              # The youngest child is Steve

```

### Arbitrary Arguments

If you do not know how many arguments will be passed into your function, you can add a `*` before the parameter name in the function definition. This will result in Python providing you a tuple of the arguments, and can be used accordingly. For Example:

```
def printLastChild(*children):
    print(f"The last child is {children[-1]}")

printLastChild("Steve", "Jim", "Bob") # The last child is Bob
```

Note: You can only have one instance of arbitrary arguments in your function

#### Valid Example

```
def my_func(fname, lname, *familyMembers):
    print(f"Hello, My Name is {fname} {lname}, My Family members are:")
    for member in familyMembers:
        print(member)
```

#### Invalid Example

```
def bad_func(*fname, *lname):
    pass
```

### Arbitrary Keyword Arguments

If you do not know many keyword arguments that will be passed into your function, you can add two asterisks: `**` before the parameter name. This will result in Python providing you a dictionary of arguments, and can be accessed accordingly:

```
def my_func(**person):
    print("Their last name is " + person["lname"])

my_func(fname = "Noel", lname = "Kocheril")
```

### Default Arguments

Sometimes we will know a good default value for a particular function, but we also want to allow the end user to change this if needed. For example:

```
def greet(name, message="Good Morning!"):
    print(f"Hello, {name}, {message}")

greet("Kate")
greet("Bruce", "How are you?")
```

Note: non-default arguments can not follow default arguments

```
def greet(message="Good Morning!", name):
    print(f"Hello, {name}, {message}")

# SyntaxError: non-default argument follows default argument
```

### Argument Data Types

When passing any data type to a function, the variable will be treated as the same data type inside the function as well. For example:

```
def my_func(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "orange"]

my_func(fruits)
```

## Return Values

Typically when creating a function, we would like to get some information back from the function based on the provided arguments. This can be done by using the keyword `return`. For example:

```
def square(x):
    return x * x

print(square(6))
print(square(7))
print(square(8))
```

Note: Once a return statement is called, the function immediately exits and does not run any more code that follows.

```
def my_func()
    return 10
    print("This will never run....")
```

## Pass

function definitions can not be empty, but if you need to have a empty function for whatever reason the keyword `pass` can be used instead.

```
def my_func():
    pass
```

## Recursion

Python also allows for function recursion, which means that a function can call itself.

Recursion is a common mathematical and programming concept, where you repeat a set of actions until you hit a specified base case.

It should be noted that it is very easy for a developer to make a mistake when using recursion and end up creating a infinite loop where the base case will never be reached. In such scenarios, we can use the keyboard shortcut `CTRL + C` to stop the program.

In the following example, we will use recursion to create a function which will return the sum of the numbers up to the provided number.

```
def sumOfNumbers(n):
    if(n >= 0):
        result = n + sumOfNumbers(n - 1)
        print(result)
    else:
        result = 0

    return result
```
