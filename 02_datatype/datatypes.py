# String is a immutable sequence of Unicode characters.
# It is used to store text data in Python.
# Strings can be created using single quotes, double quotes, or triple quotes.
# Example:
my_string = "Hello, World!"

# If a string object is defined once in memory, creating a new reference to the same string will not change the existing value.
# Strings are immutable, so any modification creates a new string object instead of changing the original.

# --- Type of String ---
print(type(90))
# --- IGNORE ---

# --- Print string and integer together ---
age = 'John'
name = 90
print('My name is', name, 'and my age is', age)
# --- IGNORE ---

# --- Understanding of pop and remove ---
numbers = [1, 2, 3, 4, 5]
numbers.pop()
numbers.remove(1)
print(numbers)
# --- IGNORE ---

# --- For Loop in Python ---
def print_square_value(numbers):
    for number in numbers:
        if number != 2:
            squared = number * number
            print(squared)

numbers = [1, 2, 3, 4]

print_square_value(numbers)
# --- IGNORE ---