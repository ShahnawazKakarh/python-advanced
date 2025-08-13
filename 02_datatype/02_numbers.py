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


# --- Understanding of floor ---
import math
# Floor function returns the largest integer less than or equal to a given number.
print("Floor of 3.7:", math.floor(3.7))  # Output: 3
print("Floor of -3.7:", math.floor(-3.7))  # Output: -4
print("Floor of 5.0:", math.floor(5.0))  # Output: 5
# --- IGNORE ---

# --- Understanding of round ---
# Round function rounds a number to the nearest integer.
# If the fractional part is exactly 0.5, it rounds to the nearest even integer.
import math
print("Round of 3.7:", round(3.7))  # Output: 4
print("Round of 3.5:", round(3.5))  # Output: 4 (nearest even)
print("Round of -3.5:", round(-3.5))  # Output: -4 (nearest even)
print("Round of 2.675:", round(2.675, 2))  # Output: 2.67 (due to floating-point precision)
# --- IGNORE ---

# --- Understanding of trunc ---
# Truncate function removes the fractional part of a number, returning the integer part.
import math
print("Truncate of 3.7:", math.trunc(3.7))  # Output: 3
print("Truncate of -3.7:", math.trunc(-3.7))  # Output: -3
print("Truncate of 5.0:", math.trunc(5.0))  # Output: 5
# --- IGNORE ---

# --- Understanding of ioata or imaginary numbers ---
# Imaginary numbers are numbers that can be expressed as a real number multiplied by the imaginary unit 'i', where i is the square root of -1.
# In Python, imaginary numbers are represented using the 'j' suffix.
# Example:
real_part = 3
imaginary_part = 4
complex_number = complex(real_part, imaginary_part)

print("Complex Number:", complex_number)  # Output: (3+4j)
print("Real Part:", complex_number.real)   # Output: 3.0
print("Imaginary Part:", complex_number.imag)  # Output: 4.0
# --- IGNORE ---

# --- Understanding of octals, hexadecimals, and binary numbers ---
# Octal numbers are base-8 numbers, hexadecimal numbers are base-16, and binary numbers are base-2.
# In Python, you can represent these numbers using prefixes:
# - Octal: prefix '0o' or '0O'
# - Hexadecimal: prefix '0x' or '0X'
# - Binary: prefix '0b' or '0B'

octal_number = 0o12  # Octal representation of 10
hexadecimal_number = 0xA  # Hexadecimal representation of 10
binary_number = 0b1010  # Binary representation of 10

print("Octal Number:", oct(octal_number))  # Output: 0o12
print("Hexadecimal Number:", hex(hexadecimal_number))  # Output: 0xa
print("Binary Number:", bin(binary_number))  # Output: 0b1010
# --- IGNORE ---

# --- Understanding of bitwise operators ---
# Bitwise operators perform operations on the binary representation of integers.
# Common bitwise operators include AND (&), OR (|), XOR (^), NOT (~), left shift (<<), and right shift (>>).
a = 5
b = 3
print("a & b:", a & b)  # Bitwise AND
print("a | b:", a | b)  # Bitwise OR
print("a ^ b:", a ^ b)  # Bitwise XOR
print("~a:", ~a)        # Bitwise NOT
print("a << 1:", a << 1)  # Left shift (multiply by 2)
print("a >> 1:", a >> 1)  # Right shift (divide by 2)
# --- IGNORE ---

# --- Understanding of random numbers ---
import random

# Random numbers can be generated using the random module in Python.
random_integer = random.randint(1, 10)
random_float = random.uniform(1.0, 10.0)

print("Random Integer:", random_integer) # Random integer between 1 and 10
print("Random Float:", random_float) # Random float between 1.0 and 10.0

# Random choice from a list
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print("Random Choice:", random_choice) # Randomly selected item from the list

# Random sample from a list
random_sample = random.sample(choices, 2)
print("Random Sample:", random_sample) # Randomly selected 2 items from the list

# Random shuffle of a list
random.shuffle(choices)
print("Shuffled Choices:", choices) # List shuffled in place
# --- IGNORE ---

# --- Understanding of Decimal Numbers ---
# Decimal numbers are used for precise decimal arithmetic, especially in financial applications.
# The Decimal class from the decimal module provides support for fast correctly-rounded decimal floating point arithmetic.
from decimal import Decimal

# Example of creating a Decimal number
decimal_number = Decimal('3.14')
print("Decimal Number:", decimal_number)  # Output: 3.14
print("Decimal Number with precision:", decimal_number.quantize(Decimal('0.01')))  # Output: 3.14
print("Decimal Number with precision 2:", decimal_number.quantize(Decimal('0.001')))  # Output: 3.140
# Decimal numbers can be created from strings to avoid floating-point representation issues.

# Example:
decimal_from_string = Decimal('0.1') + Decimal('0.2')
print("Decimal from String:", decimal_from_string)  # Output: 0.3
# --- IGNORE ---

# --- Understanding of Fraction Numbers ---
# Fraction numbers represent rational numbers as a pair of integers: a numerator and a denominator.
# The Fraction class from the fractions module provides support for rational number arithmetic.
# Example of creating a Fraction
from fractions import Fraction

fraction_number = Fraction(3, 4)  # Represents 3/4
print("Fraction Number:", fraction_number)  # Output: 3/4
print("Numerator:", fraction_number.numerator)  # Output: 3
print("Denominator:", fraction_number.denominator)  # Output: 4
# Fraction numbers can be created from integers, floats, or strings.

# Example:
fraction_from_float = Fraction(0.75)
print("Fraction from Float:", fraction_from_float)  # Output: 3/4

fraction_from_string = Fraction('1.5')
print("Fraction from String:", fraction_from_string)  # Output: 3/2

# Fraction arithmetic
fraction_sum = Fraction(1, 2) + Fraction(1, 3)
print("Sum of Fractions:", fraction_sum)  # Output: 5/6
# --- IGNORE --- 

# --- Understanding of Union, Intersection, and Difference of Sets ---
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Elements in either set
union_set = set_a | set_b
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements in both sets
intersection_set = set_a & set_b
print("Intersection:", intersection_set)  # Output: {3, 4}

# Difference: Elements in set_a but not in set_b
difference_set = set_a - set_b
print("Difference (set_a - set_b):", difference_set)  # Output: {1, 2}
# --- IGNORE ---

