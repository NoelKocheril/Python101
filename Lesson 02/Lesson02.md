# Lesson 02 - Basic Python Syntax

## Table of Contents

1. [What is Syntax?](#what-is-syntax)

## What is Syntax? <a id="what-is-syntax" name="what-is-syntax"></a>

Within a programming language, syntax is the set of rules that defines how the combinations of symbols can be structured to create statements and/or expressions. In order to make sure both the programming language and the developer are able to create end product, they both must agree to the same set of rules in which the source code is written. However, it is to be noted that the programming language will take every instance of source code literally and just because the developer thinks something should interact a certain way does not necessarily mean that is what the source code will do.

For Example:

When Looking at the following code:

```
'a' + 1
```

What does it mean to add a number to a letter? Should we interpret this as concatenating the two strings "a" and "1" together? Should this result in an error? Should 'a' be converted into a number?

Note 1: Python is a dynamically typed language and issues like this will crop up very often which will only present itself at Run Time (when the code is executing).

Note 2: Python handles this situation by raising an TypeError exception (We will get into the details of this later).

## Creating a Variable

### What is a variable?

In a programming language context, a variable is a reference to a some data that can be changed, altered, and used at a later point.

### Using Variables

Within Python, we can create variables using the "=" operator. For example::

```
Name = "Noel Kocheril"
Age = 24
FavoritePlaces = ["Denny's", "Home", "Gym"]
```

The above code creates three separate variables, one that is a String that contains my name, and one that contains my current age, and the last one that contains a list of my favorite places.

We can use these variables at a later point in our code, for example:

```
print(Name) # Noel Kocheril
```

We can also re-assign a variable to a different as needed, for example:

```
x = 4
x = "Sally"
print(x) # Sally
```

We will return to variables at a later point in our course.

## Indentation

An Important Concept within Python is Indentation. Indentation refers to the spaces at the beginning of a line of code. In other programming languages, Indentation is used only for readability purposes; Python uses Indentation to denote blocks of code.

For Example:

```
if 5 > 2:
    print("Five is Greater than two")
```

The print statement is a block of code that is a part of the previous indentation level (the IF Statement).

If we do not provide the correct indentation level, Python will return an error.

```
if 5 > 2:
print("Five is Greater than two") # IndentationError: expected an indented block after 'if' statement on line ##
```

The number of indentation is upto you as a developer, but it is suggested that you remain consistant.

```
if 5 > 2:
    print("Five is Greater than two") # IndentationError: expected an indented block after 'if' statement on line ##
if 5 > 2:
        print("Five is Greater than two") # IndentationError: expected an indented block after 'if' statement on line ##
```

However, it is be noted that you must maintain the same level of indentation through each of your code blocks, for example:

```
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!") # IndentationError: unexpected indent
```

Note: To Quickly Indent your code in VS Code, you can use the shortcut keys \
Indent: CTRL + ] \
Dedent: CTRL + [

## Comments

Comments within Python are denoted by the pound/hashtag symbol (#). Any symbols after the pound symbol are ignored by the language and can be used to improve readability, add context, and quickly disable blocks of code. 

Comments can be added at any point in a line of code, for example:

```
# This is a valid comment
print("Hello") # This is a valid comment
```

Note: Within VS Code, you can quickly comment out a block of code using the shortcut key CTRL + SHIFT + /

## Typing

### Statically Typed vs Dynamically Typed

As previously mentioned Python is a dynamically typed language, but what exactly does that mean? 

A programming language is deemed to be a dynamically typed language when the variables are assigned a type at runtime rather than at compile time.

For Example: 

Statically Typed Language, i.e. Java, C, C++
```
int x = 5;
```

Dynamically Typed Language, i.e. Python, JavaScript, Lua
```
x = 5;
```

Note: In a statically typed language we specific the type of the variable when it's created, but in a dynamically typed language the compiler will figure that for us once it begins running the code.

What are the implications of using a dynamically typed language?

You are able to use the same variable for multiple purposes, for example:

```
x = 5
x = "Hello, World"
x = ["This", "is", "an", "array"]
```

This is a level of abstraction that is removed from the developer by the language, but can also be the cause of potential pit falls when a variable is overused unnecessarily.

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
my_set = ["Noel", 3, [5]]
```




