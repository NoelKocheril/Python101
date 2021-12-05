# Exercise 2.4 Fibonacci Sequence
#
# The Fibonacci sequence is a series of numbers where the next number is found by adding the two numbers before it.
#
# The first two numbers are 0 and 1.
#
# For example: 0, 1, 1, 2, 3, 5, 8, 13, 21

# Initialize the two numbers to 0 and 1.
num1, num2 = 0, 1

# Loop through the numbers
for i in range(20):
    # Find the new result
    res = num1 + num2

    # Print out the result
    print(res)

    # Update the num1 and num2 to num2 and res
    num1 = num2
    num2 = res
