# Numbers in python are immutable data types.
# They can be integers, floats, or complex numbers.
# Integers are whole numbers, floats are decimal numbers, and complex numbers have a real and imaginary part.
# Example:
my_integer = 42
my_float = 3.14
my_complex = 1 + 2j

# Numbers can be used in arithmetic operations like addition, subtraction, multiplication, and division.
# Example:
sum_result = my_integer + my_float
product_result = my_integer * my_float

print("Sum:", sum_result)
print("Product:", product_result)

# Numbers can also be converted to strings for display purposes.
# Example:
number_as_string = str(my_integer)
print("Number as String:", number_as_string)
# --- IGNORE ---

# Operater overloading in Python
print(3 + 4)       # Addition for integers
print("Shahnawaz" + "Khan")   # Concatenation for strings
# --- IGNORE ---

# calculate reminder, power, and floor division
a = 10
b = 3

remainder = a % b          # Remainder of division
power = a ** b             # Power operation
floor_division = a // b    # Floor division

print("Remainder:", remainder)
print("Power:", power)
print("Floor Division:", floor_division)
# --- IGNORE ---

# Difference between repr , str , print and format
# repr() is used to get a string representation of an object that can be used for debugging.
# str() is used to get a user-friendly string representation of an object.
# print() outputs the string representation to the console.
# format() is used to format strings with placeholders.

my_number = 42
print("Using repr:", repr(my_number))  # Debugging representation
print("Using str:", str(my_number))    # User-friendly representation
print("Using print:", my_number)        # Direct output
formatted_string = "The number is: {}".format(my_number)  # Formatted string
print("Using format:", formatted_string)

# repr() → Make it precise & unambiguous (good for debugging, logging)
# str() → Make it pretty & readable (good for the end-user)
# --- IGNORE ---

# --- Type of Number ---
print(type(90))        # Integer
print(type(3.14))      # Float
print(type(1 + 2j))    # Complex Number
# --- IGNORE ---

# --- Print string and integer together ---
age = 25
name = 'John'
print('My name is', name, 'and my age is', age)
# --- IGNORE ---

#  --- Understanding of comparison operators ---
a = 10
b = 20

print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to
print("a is b:", a is b)     # Identity (same object)
print("a is not b:", a is not b)  # Identity (not the same object)
print("a in b:", a in [10, 20, 30])  # Membership (is a in the list)
print("a not in b:", a not in [20, 30, 40])  # Membership (is a not in the list)
# --- IGNORE ---

# --- Understanding of augmented assignment operators ---
x = 5
print("Initial x:", x)

x += 3  # Equivalent to x = x + 3
print("After x += 3:", x)

x -= 2  # Equivalent to x = x - 2
print("After x -= 2:", x)

x *= 4  # Equivalent to x = x * 4
print("After x *= 4:", x)

x /= 3  # Equivalent to x = x / 3
print("After x /= 3:", x)

x //= 2 # Equivalent to x = x // 2 (floor division)
print("After x //= 2:", x)

x %= 3  # Equivalent to x = x % 3 (modulus, remainder)
print("After x %= 3:", x)

x **= 2 # Equivalent to x = x ** 2 (exponentiation, power)
print("After x **= 2:", x)
# --- IGNORE ---

