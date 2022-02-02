# Lesson 05 - Classes

Python is an object oriented (OO) programming language. This means that almost everything in Python is an object, which holds properties and methods. A class is like a blueprint for such an object.

## Creating a class

In order to create a class, we must use the `class` keyword. For example:

```
class MyClass:
    x = 5
```

## Creating an object

Now that we have a class, we can create an object of that class. For example:

```
o1 = MyClass()
print(o1.x)
```

## The \_\_init\_\_ function

The above example is the most simple class we can create, but this results in it not being useful in an actual real life application.

In order for a class to be a bit more useful, we need to utilize a few features within Python to make it so that objects can be created a bit more dynamically and generically.

We can use the `__init__` function to create various objects with a similar blueprint but different values. For example:

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Noel", 25)
p2 = Person("Vit", 25)

print(p1.name)
print(p2.age)
```

Note 1: When calling the Person constructor [`Person(...)`], python will automatically use the provided `__init__` function. If no `__init__` function is provided, python will use the default constructor.

Note 2: The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

## Inheritance

Inheritance
