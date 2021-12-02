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
