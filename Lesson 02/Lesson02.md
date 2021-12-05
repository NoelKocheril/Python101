# Lesson 02 - Basic Python Syntax and Data Structures

## Table of Contents

1. [What is Syntax?](#what-is-syntax)

## What is Syntax? <a id="what-is-syntax" name="what-is-syntax"></a>

Within a programming language syntax is the set of rules that defines how the combinations of symbols can be structured to create statements and/or expressions. In order to make sure both the programming language and the developer are able to create end product, they both must agree to the same set of rules in which the source code is written. However, it is to be noted that the programming language will take every instance of source code literally and just because the developer thinks something should interact a certain way does not necessarily mean that is what the source code will do.

For example, when looking at the following code:

```
'a' + 1
```

What does it mean to add a number to a letter? Should we interpret this as concatenating the two strings "a" and "1" together? Should this result in an error? Should 'a' be converted into a number? If so, what should the letter 'a' to equal to as a number?

Note 1: Python is a dynamically typed language and issues like this will crop up very often which will only present itself at run time (when the code is executing), like when trying to add two varaibles together.

Note 2: Python handles this situation ("'a' + 1") by raising an TypeError exception. (We will get into the details of this at a later point in the course)

## Creating a Variable

### What is a variable?

In a programming language context, a variable is a reference to a some data that can be changed, altered, and used at a later point.

### Using Variables

Within Python, we can create variables using the assignment operator ("="). For example:

```
Name = "Noel Kocheril"
Age = 24
FavoritePlaces = ["Denny's", "Home", "Gym"]
```

The above code creates three separate variables, one that is a string that contains my name, and one that contains my current age, and the last one that contains a list of my favorite places.

We can use these variables at a later point in our code, for example:

```
print(Name) # Noel Kocheril
```

We can also re-assign a variable to a different value as needed, for example:

```
x = 4
x = "Sally"
print(x) # Sally
```

We will return to variables and types at a later point in our course.

### Excerise 2.1: Creating a variable and print it out

In this excerise, I would like you to create three variables:

1. Your Name
2. Your Age
3. A list of places you like

and print them out with a blurb before each. For example, "My Name is: {Name}".

Note: You can convert an integer or a list to a string by using the str() function.

You can see the solution [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Solutions/Exercise2_1.py).

## Indentation

An important concept within Python is indentation. Indentation refers to the spaces at the beginning of a line of code. In other programming languages, indentation is used purely for readability purposes; Python, however, uses indentation to denote blocks of code.

For example:

```
if 5 > 2:
    print("Five is greater than two.")
```

Note: Using Spaces and Tabs will provide different levels of indentation, luckily VS Code will auto-convert this for you. You should be careful when using other IDEs or the command line that do not correct this for you.

The print statement is a block of code that is a part of the previous indentation level (the IF statement).

If we do not provide the correct indentation level, Python will return an error:

```
if 5 > 2:
print("Five is greater than two.") # IndentationError: expected an indented block after 'if' statement on line ##
```

The number of indentation is upto you as a developer, but it is suggested that you remain consistant throughout your code.

```
if 5 > 2:
    print("Five is greater than two.")
if 5 > 2:
        print("Five is greater than two.")
```

However, it is be noted that you must maintain the same level of indentation through each of your code blocks, for example:

```
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!") # IndentationError: unexpected indent
```

Note: To quickly indent your code in VS Code, you can use the shortcut keys \
Indent: CTRL + ] \
Dedent: CTRL + [

We can also have multiple levels of indentation, for example:

```
x = 100

if x > 5:
    print("X is greater than 5")
    if x > 10:
        print("X is greater than 10")
        if x > 20:
            print("X is greater than 20")
```

### Excerise 2.2 Fix the indentation in this code

Without the use of the auto-indentation correction from VS Code, fix the below indentation from [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Problems/Exercise2_2.py).

You can see the solution [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Solutions/Exercise2_2.py).

## Comments

Comments within Python are denoted by the pound/hashtag symbol ("#"). Any symbols after the pound/hashtag are ignored by the language and can be used to improve readability, add context, and quickly disable blocks of code.

Comments can be added at any point in a line of code, for example:

```
# This is a valid comment
print("Hello") # This is a valid comment
```

Note: Within VS Code, you can quickly comment and uncomment out a block of code using the shortcut key "CTRL + /"

## Conditional Statements

### Basic If Statement

The basic "if" statement in it's simplest form would look like:

```
if <expr>:
    <statement>
```

In the above form, &lt;expr&gt; is an expression that will be evaluated as boolean and if it is "truthy", we will evaluate the code in the &lt;statement&gt;.

Note 1: The colon after the expression is required.

Note 2: We will discuss "truthy" and "falsy" at a later point in the course. For now, if the expression is equal to true we will do one block of statements.

Code that is outside of the indented code block will be executed regardless of whether the expression is true or false.

```
if 4 > 5:
    print("This will not print")
print("This will always print.")
```

### If Else

The basic "if" statement can be expanded to do one set of code if our expression is equal to True and another if it is equal to False. This is accomplished using the "else" keyword:

```
if <expr>:
    <statement1>
else:
    <statement2>
```

If the expression is true, then we will execute the code that is in statement1 and if the expression is false, we will execute the code that is in statement2. For example:

```
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

# (first suite)
# x is small
```

```
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

# (second suite)
# x is large
```

### Elif statements

If we need to do different statements based on various expressions, we can utilizes the elif keyword. For example:

```
if <expr1>:
    <statement1>
elif <expr2>:
    <statement2>
elif <expr3>:
    <statement3>
...
else:
    <statement>
```

An actual use case of this would be to have multiple constraints like when looking at grades:

```
grade = int(input("Enter Grade Percentage: "))

if (grade <= 100) and (grade >= 80):
    print("You got an A")
elif (grade < 80) and (grade >= 70):
    print("You got an B")
elif (grade < 70) and (grade >= 60):
    print("You got an C")
elif (grade < 60) and (grade >= 50):
    print("You got an D")
elif (grade < 50) and (grade >= 0):
    print("You got an F")
else:
    print("Invalid grade")
```

## Data Structures

### List

A list is a sequence of data that can be stored within a single object.

A list is ordered, changeable/mutable, and allow for duplicate values.

A list can be created via the following code:

```
my_list = ["Noel", "Steve", "Jim"]
```

A list is created with square brackets.

Note: Python does not require all items in the list to be of the same type.

```
my_list = ["Noel", 3, [5]]
```

### Tuple

A tuple can also be used to store multiple values in a single object.

A tuple is ordered, _*unchangeable/immutable*_, and allow for duplicate values.

```
my_tuple = ("Noel", "Steve", "Jim")
```

A list is created with round brackets.

Like a list, a tuple can have multiple values of multiple types.

Note: In order to create a tuple with a single element, you must include a trailing comma

```
tuple1 = ("apple",)
print(type(tuple1))

#NOT a tuple
tuple2 = ("apple")
print(type(tuple2))
```

### Set

A set is a group of data that can be stored within a single object.

A set is _*unordered*_, _*unchangeable/immutable*_, and _*does not allow*_ for duplicate values.

A set can be created via the following code:

```
my_set = {"Noel", "Steve", "Jim"}
```

A set is created with curly brackets.

If you try to create a set with duplicate values, you will end up with only one instance of the value. For Example:

```
my_set = {"Noel", "Steve", "Noel"}
print(my_set) # {'Steve', 'Noel'}
```

Note: Python does not require all items in the set to be of the same type.

```
my_set = {"Noel", 3, [5]}
```

### Dictionary

A dictionary is a set of key-value pairs that can be used to store multiple sets of data in a single object.

A dictionary is ordered, changeable/mutable, and _*does not*_ allow for duplicate values.

A dictionary can be created via the following code:

```
my_list = {"Name": "Noel", "Friend": "Steve", "Enemy": "Jim"]
```

A dictionary is created with curly brackets where the first object before the colon is the key and object after the colon is value.

Unlike Lists, Sets, and Tuples dictionaries are accessed using the key object rather than an index.

Like a set, if we try to create a dictionary with two repeating keys. We end up with a dictionary with the most recent assignment for the given key. For Example:

```
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(my_dict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```
