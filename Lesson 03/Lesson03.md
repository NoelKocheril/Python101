# Lesson 03 - Typing and Data Structure

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

## General Types

### Note: Python will try to figure out what the type of any variable is, and you do not need to specific what the type is like in other programming languages. However, it should be noted that specificizing the type can help prevent potential issues that may come up in the future. For example, if your program expects a number but you provide a word (also known as a string) your IDE can pick up on that quicker.

### Integer (int)

### float

### string (str)

### boolean (bool)

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
