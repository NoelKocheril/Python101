# Lesson 02 - Basic Python Syntax, If Statements, and Loops

## Table of Contents

1. [What is Syntax?](#what-is-syntax)

## What is Syntax? <a id="what-is-syntax" name="what-is-syntax"></a>

Within a programming language syntax is the set of rules that defines how the combinations of symbols can be structured to create statements and/or expressions. In order to make sure both the programming language and the developer are able to create end product, they both must agree to the same set of rules in which the source code is written. However, it is to be noted that the programming language will take every instance of source code literally and just because the developer thinks something should interact a certain way does not necessarily mean that is what the source code will do.

For example, when looking at the following code:

```
'a' + 1
```

What does it mean to add a number to a letter? Should we interpret this as concatenating the two strings "a" and "1" together? Should this result in an error? Should 'a' be converted into a number? If so, what should the letter 'a' to equal to as a number?

Note 1: Python is a dynamically typed language and issues like this will crop up very often which will only present itself at run time (when the code is executing), like when trying to add two variables together.

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

### Exercise 2.1: Creating a variable and print it out

In this exercise, I would like you to create three variables:

1. Your Name
2. Your Age
3. A list of places you like

and print them out with a blurb before each. For example, "My Name is: {Name}".

Note: You can convert an integer or a list to a string by using the str() function.

Starter File for this exercise can be found [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Problems/Exercise2_1.py)

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

The number of indentation is up to you as a developer, but it is suggested that you remain consistent throughout your code.

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
Indent: "CTRL + ]" \
Dedent: "CTRL + ["

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

### Exercise 2.2 Fix the indentation

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

### Exercise 2.3 Exam Attendance Checker

A student is only allowed to attend the exam if their attendance is greater than or equal to 75%.

Take the following inputs from the user:

1. The number of classes held.
2. The number of classes attended.

and print:

1. The percentage of classes attended.
2. Whether or not the student is allowed to attend the exam.

Note: You can get input from the user via the function input()

```
# The input function gets the input from the user, the int function converts the input to a number
numberOfClassesHeld = int(input("Enter the number of classes held: "))
```

Starter File for this exercise can be found [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Problems/Exercise2_3.py)

You can see the solution [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Solutions/Exercise2_3.py).

## Loops

Within programming, we tend to want to write similar logic across multiple values. For Example, looping from one to a hundred or a list of objects and doing a set of instructions on each value. In order to do this, we can employ different types of loops like the "for" loop and the "while" loop.

### For Loops

The for loop can be used to loop through an iterable object such as a list, a string, or a dictionary. For example:

```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# apple
# banana
# cherry
```

If we were to attempt to use the same logic for a string, we would get each character in the string. For example:

```
for x in "banana":
    print(x)

# b
# a
# n
# a
# n
# a
```

Within python, in order to quickly loop through a set of numbers we can use the function "range". For example:

```
for x in range(6):
    print(x)

# 0
# 1
# 2
# 3
# 4
# 5
```

Note: the range function will go from values from 0 to 5, not 0 to 6

We can also add an extra parameter to the range function in order to start from a different value. For example:

```
for x in range(2, 6):
    print(x)

# 2
# 3
# 4
# 5
```

### While Loops

A while loop can be used when we don't necessarily know when the loop should end. The loop will keep running while the condition it is provided is true. For example:

```
i = 1
while i < 6:
    print(i)
    i += 1
```

Note: It is very important that we increment i, otherwise the loop will continue to run forever. If you are in this scenario, you can typically hit "CTRL + C" to stop your program.

### Nested Loops

A nested loop is a situation where we have a loop inside of another loop. These are typically used for working with multiple dimensions lists like in a table. When we have a nested loop, the inner loop will be repeated from the beginning with every iteration of the outer loop.

For example:

```
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "orange"]

for x in adjectives:
    for y in fruits:
        print(x, y)

# red apple
# red banana
# red orange
# big apple
# big banana
# big orange
# tasty apple
# tasty banana
# tasty orange
```

### break

Occasionally we will want to preemptively exit out of a loop, in order to do this we can use the "break" keyword. For example:

```
fruits = ["apple", "banana", "orange"]

for x in fruits:
    print(x)
    if x == "banana":
        break

# apple
# banana
```

### continue

In order scenarios, we will want to just skip over the current iteration rather than stop the loop completely. This can be completed with the "continue" keyword. For example:

```
fruits = ["apple", "banana", "orange"]

for x in fruits:
    if x == "banana":
        continue
    print(x)

# apple
# orange
```

### pass

Loops can not be empty, but if for whatever reason you have a loop with no content you can put in the "pass" keyword to avoid getting an error. For example:

```
for x in [1, 2, 3]:
    pass
```

### else with a loop

The "else" keyword can be used to execute code when a loop is finished. For example:

```
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!
```

Note: The "else" block will not be executed when the loop is stopped using the break statement.

```
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!") # This will never be executed.

# 0
# 1
# 2
```

### Exercise 2.4 Fibonacci Sequence

The Fibonacci sequence is a series of numbers where the next number is found by adding the two numbers before it.

The first two numbers are 0 and 1.

For example: 0, 1, 1, 2, 3, 5, 8, 13, 21

print out the first 20 digits in the sequence.

Starter File for this exercise can be found [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Problems/Exercise2_4.py)

You can see the solution [here](https://github.com/NoelKocheril/Python101/blob/main/Lesson%2002/Solutions/Exercise2_4.py).
