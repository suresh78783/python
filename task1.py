# 1) how to diclare different types of data types in python
# Integer
my_int = 10

# Float
my_float = 10.5

# String
my_string = "Hello, World!"

# Boolean
my_bool = True

# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Dictionary
my_dict = {"name": "Alice", "age": 25}

# Set
my_set = {1, 2, 3, 4, 5}

# NoneType
my_none = None


# 2) Types of operators in Python with examples

# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Modulus:", a % b)         # Modulus
print("Exponentiation:", a ** b) # Exponentiation
print("Floor Division:", a // b) # Floor Division

# Comparison Operators
print("Equal:", a == b)          # Equal
print("Not Equal:", a != b)      # Not Equal
print("Greater than:", a > b)    # Greater than
print("Less than:", a < b)       # Less than
print("Greater than or equal to:", a >= b) # Greater than or equal to
print("Less than or equal to:", a <= b)    # Less than or equal to

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)   # Logical AND
print("Logical OR:", x or y)     # Logical OR
print("Logical NOT:", not x)     # Logical NOT

# Bitwise Operators
c = 6  # 110 in binary
d = 2  # 010 in binary
print("Bitwise AND:", c & d)     # Bitwise AND
print("Bitwise OR:", c | d)      # Bitwise OR
print("Bitwise XOR:", c ^ d)     # Bitwise XOR
print("Bitwise NOT:", ~c)        # Bitwise NOT
print("Bitwise left shift:", c << 1)  # Bitwise left shift
print("Bitwise right shift:", c >> 1) # Bitwise right shift

# Assignment Operators
e = 5
e += 3  # e = e + 3
print("Assignment (+=):", e)
e -= 2  # e = e - 2
print("Assignment (-=):", e)
e *= 2  # e = e * 2
print("Assignment (*=):", e)
e /= 2  # e = e / 2
print("Assignment (/=):", e)
e %= 3  # e = e % 3
print("Assignment (%=):", e)
e **= 2  # e = e ** 2
print("Assignment (**=):", e)
e //= 2  # e = e // 2
print("Assignment (//=):", e)

# Identity Operators
print("Identity (is):", a is b)  # Identity (is)
print("Identity (is not):", a is not b)  # Identity (is not)

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Membership (in):", 3 in my_list)  # Membership (in)
print("Membership (not in):", 6 not in my_list)  # Membership (not in)


# 3) Conditional Statements in Python

# Conditional statements are used to perform different actions based on different conditions.
# The if, elif, and else statements are used for this purpose.

# Example of if statement
num = 10
if num > 0:
    print("The number is positive")

# Example of if-else statement
num = -5
if num > 0:
    print("The number is positive")
else:
    print("The number is non-positive")

# Example of if-elif-else statement
num = 0
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")



# 4) Functions in Python
# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result.
# Declaring a function
def greet(name):
    return f"Hello, {name}!"
# Calling a function
result = greet("Suresh")
print(result)  # Output: Hello, Suresh!
# Example of a function with a return statement
def add(a, b):
    return a + b
# Calling the function
sum_result = add(10, 5)
print("Sum:", sum_result)  # Output: Sum: 15


# 5) Inbuilt Functions in Python
# Python has several inbuilt functions that are readily available for use.
# Here are some examples of commonly used inbuilt functions for strings and lists:

# String Functions
my_string = "Hello, World!"
# len() - returns the length of the string
print("Length of string:", len(my_string))

# lower() - converts the string to lowercase
print("Lowercase string:", my_string.lower())

# upper() - converts the string to uppercase
print("Uppercase string:", my_string.upper())

# replace() - replaces a substring with another substring
print("Replaced string:", my_string.replace("World", "Python"))

# split() - splits the string into a list of substrings
print("Split string:", my_string.split(", "))


# List Functions
my_list = [1, 2, 3, 4, 5]
# len() - returns the number of elements in the list
print("Length of list:", len(my_list))
# append() - adds an element to the end of the list
my_list.append(6)
print("List after append:", my_list)
# remove() - removes the first occurrence of an element from the list
my_list.remove(3)
print("List after remove:", my_list)
# pop() - removes and returns the last element of the list
print("Popped element:", my_list.pop())
print("List after pop:", my_list)
# sort() - sorts the elements of the list in ascending order
my_list.sort()
print("Sorted list:", my_list)