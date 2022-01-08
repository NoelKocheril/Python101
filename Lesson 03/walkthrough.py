x = 5
print(x)

x = "Hello World"
print(x.upper())

x = ["Weeeeeee", "werwerwerwe"]
print(x)

x = 123

y = 1 + 2

x = "Hello Wotrl 2131!@21312323423423, ,,,,"
# x = "asdasdasd' " # This doesn't work

x = "My dog's name is steve"

# x = 'My dog's name is steve'


x = "Hrellorwerw"


print(x)
x = """asjdhaskjdhasdkj

asdasdhasjkdhask

ashd"""

print(x.upper())


y = 0.5123123
z = 3.5

z = 1 / 3 + 2 / 3
print(z)

# 1/2, 1/4, 1/8
# 1/10,

True or False


z = 123123

print("Hello" == "Hello")  # True
print("Hello" == "hello")  # False

print(1 == 1)
print(1 >= 3)
print(2 <= 3)
print(1 != 2)

# List

my_list = [1212312, "asdasdhgasd", 233.123123, [123123, "perti"]]

tictactoe = [["X", "", "O"], ["X", "O", ""], ["X", "", ""]]

print(tictactoe)


# Lists are Ordered

places = ["India", "Japan", "America"]


print(places[0])
print(places[1])

for i in range(3):
    print(i)
    print(places[i])


# print(places[4]) # Index Error: went out of range
print(places[-2])


# Lists can have duplicates

my_list = [1, 1, 2, 2]

# Lists are mutable / changable

my_list[0] = 4

print(my_list)


# Tuple

my_tuple = (1, 2, 3, "asdasdhjkasd", 0.3423423)

# Difference between tuple and list, you can't change items in a tuple

print(my_tuple[0])

# my_tuple[1] = 4

print(my_tuple)

# tuple - single item tuples need to have a trailing comma

my_tuple = (2,)

my_num = (2 + 3) * 4


print(type(my_tuple))

# Set

my_set = {"Hello", 213123, 345.34523423}

print(my_set)

my_set = {"Set", "Set", 213123, 345.34523423}
print(my_set)


for item in my_set:
    print(f"The item is: {item}")

print(f"The items are: {my_set}")


# Dictionary

my_dict = {"Name": "Noel Kocheril", "Age": 25, "Address": "50 Bayhampton Drive"}
my_dict = {
    "Name": "Noel Kocheril",
    "Age": 25,
    "Address": "50 Bayhampton Drive",
    "Test": "Noel Kocheril",
    "Name": "Arjun Malhi",
}
print(my_dict)

my_dict["Name"] = "Vithusan Vimal"

print(my_dict)
