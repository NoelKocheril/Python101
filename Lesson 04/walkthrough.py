# Defines a function
# def my_func():
#     print("Hello, World!")


# Calls a function
# my_func()


# Repeats a function
# for j in range(10):
#     my_func()


# myName = "Noel Kocheril"


# def hello(fname):
#     print(f"Hello {fname}")


# hello() # Missing an argument

# hello("Noel")
# hello("Vit")
# hello("Shawn")

# Takes two arguments, and adds them together
# def sum(x, y):
#     print(x + y)


# def difference(x, y):
#     print(x - y)


# def difference2(x, y, z):
#     print(x - y)


# difference(5, 10)
# difference(y=5, x=10)
# difference2(10, 5)

# x = 5
# print("Hello", "Noel", x)


# def printLastChild(*children):
#     print(children[-1])


# printLastChild("Noel", "Steve", "Bob")

# Not allowed to have multiple arbitrary arguments
# def printNames(*fname, *lnames):
#     print(f"{fname} {lnames}")


# def printLastName(**person):
#     print("Hello, Mr. " + person["lname"])


# printLastName(fname="Noel", age=25, lname="Kocheril")


# def greet(name, message="Good Morning!"):
#     print(f"Hello, {name}, {message}")


# greet("Noel")
# greet("Vit", "How are you?")


# Not allowed: Non-Default Argument after default argument
# def greet(message="Good Morning!", name):
#     print(f"Hello, {name}, {message}")


# def my_func(food):
#     for x in food:
#         print(x)


# fruits = ["apple", "banana", "orange"]

# my_func(fruits)


# def square(x):
#     return x * x


# print(square(10))


# def my_func():
#     return 4
#     print("This will never run.....")


# def percentageToLetterGrade(percentage):
#     if percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     return "F"


# print(percentageToLetterGrade(50))


# def sumOfNumbers(n):
#     if n >= 0:
#         result = n + sumOfNumbers(n - 1)
#         print(result)
#     else:
#         result = 0

#     return result


# sumOfNumbers(5)


# """

# sumOfNumbers(5)
# -> result = 5 + sumOfNumbers(4)
# -> result = 5 + 4 + sumOfNumbers(3) -> 0


# """


# def TowersOfHanoi()

# Fibonacci Sequence - n = n-1 + n-2

# x_n = x_n-1 + x_n-2

# count = 0


# def FibonacciSequence(n):
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         result = FibonacciSequence(n - 1) + FibonacciSequence(n - 2)

#     global count
#     count += 1

#     print(result)
#     return result


# FibonacciSequence(10)
# print(count)

# for i in range(100):
#     print(f"{i}: {FibonacciSequence(i)}")

# def fib(n):
#     if n


# sum = 0

# for i in range(1, 10):
#     sum += 2 ** i

# print(sum)

"""

fib(n) -> fib(n-1) + fib(fib-2)

1 - fib
2 - 2 fib
3 - 4 fib
nth - 2^n - 17,179,869,184

"""


# Power Function - Using Recursion
# power(base, expo)

# x^n
# def power(base, expo):
#     if expo > 0:
#         result = power(base, expo - 1) * (base)
#         print(result)
#         return result
#     elif expo == 0:
#         return 1


# power(3, 3)


"""

power(3,3)
result = 27


"""

"""

STEP 1
N^6
->
(N^5 * N)

STEP 2
N^5 * N
->
(N^4 * N) * N


(N^3 * N) * N * N
(N^2 * N) * N * N * N
(N^1 * N) * N * N * N * N
(N^0 * N) * N * N * N * N * N 
1   * N * N * N * N * N * N 

"""
# always comes back to sequences

# Factorial - n! = n * (n - 1)!


def factorial(x):
    if x > 0:
        result = x * factorial(x - 1)
        print(result)
        return result
    elif x == 0:
        return 1


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


for i in range(5):
    fact(i)


"""""
n! 
 
4! = 4*3*2*1
4! 
3! = 3*2*1

4!
4 * 3!
4 * 3 * 2!
4 * 3 * 2 * 1!
4 * 3 * 2 * 1 * 0!
4 * 3 * 2 * 1 * 1


"""
