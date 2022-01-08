# String Repeat
#
# Get two inputs from the user
# 1. The number of times to repeat
# 2. The string to repeat

numRepeat = int(input("Enter the number of times to repeat: "))
stringRepeat = input("Enter the string to repeat: ")

# Solution 1:
for i in range(numRepeat):
    print(stringRepeat, end="")

# Solution 2
res = ""
for i in range(numRepeat):
    res += stringRepeat
print(res)
