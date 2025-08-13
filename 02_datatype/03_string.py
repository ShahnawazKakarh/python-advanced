# Strings in Python
# Strings are immutable sequences of Unicode characters.
# They are used to store text data in Python.
# Strings can be created using single quotes, double quotes, or triple quotes.

my_string = "Hello, World!" # Example of a string

# Get first character of the string
first_character = my_string[0]  # Accessing the first character
print(first_character)  # Output: "H"

# Get a substring from the string
substring = my_string[7:12]  # Accessing a substring from index 7 to 11
print(substring)  # Output: "World"

# Practice
num_list = "0123456789"  # Example of a string containing numbers
# Get the first character of num_list
first_num = num_list[0]  # Accessing the first character
print(first_num)  # Output: "0"

one_to_five = num_list[1:5]  # Get a substring from index 1 to 4
print(one_to_five)  # Output: "1234"

entire_string = num_list[:] # Get the entire string
print(entire_string)  # Output: "0123456789"

first_seven = num_list[:7] # Get the first seven characters of the string
print(first_seven) # Output: "0123456"


# If a string object is defined once in memory, creating a new reference to the same string will not change the existing value.
# Strings are immutable, so any modification creates a new string object instead of changing the original.
# For example, if you try to change a character in a string, it will result in an error.
# Instead, you can create a new string with the desired changes.
# Example of string immutability
try:
    my_string[0] = 'h'  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
# To modify a string, you can create a new one
new_string = 'h' + my_string[1:]  # This creates a new string with the first character changed
print(new_string)  # Output: "hello, World!"

# Strings can be concatenated using the '+' operator
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"  # Concatenation
print(full_greeting)  # Output: "Hello, Alice!"

# You can also use formatted strings (f-strings) for more complex string formatting
age = 30
formatted_string = f"{name} is {age} years old."  # Using f-string for formatting
print(formatted_string)  # Output: "Alice is 30 years old."

# Strings support various methods for manipulation, such as upper(), lower(), split(), join(), etc.
uppercase_string = my_string.upper()  # Convert to uppercase
print(uppercase_string)  # Output: "HELLO, WORLD!"

lowercase_string = my_string.lower()  # Convert to lowercase
print(lowercase_string)  # Output: "hello, world!"

words = my_string.split(", ")  # Split the string into a list of words
print(words)  # Output: ['Hello', 'World!']

joined_string = " ".join(words)  # Join the list back into a string
print(joined_string)  # Output: "Hello World!"

# Strings can also be checked for membership using the 'in' keyword
contains_hello = "Hello" in my_string  # Check if "Hello" is in the string
print(contains_hello)  # Output: True

# You can find the length of a string using the len() function
string_length = len(my_string)  # Get the length of the string
print(string_length)  # Output: 13

# Strings can be indexed and sliced like lists
first_character = my_string[0]  # Get the first character
print(first_character)  # Output: "H"

substring = my_string[7:12]  # Get a substring from index 7 to 11
print(substring)  # Output: "World"

# Strings can also be iterated over in a loop
for char in my_string:
    print(char, end=' ')  # Print each character in the string
# Output: H e l l o ,   W o r l d !
print()  # New line after the loop 

# Another example of string iteration in loop without end parameter
for char in my_string:
    print(char)  # Print each character on a new line
# Output:
# H
# e
# l
# l
# o
# ,
##  
# W
# o
# r
# l
# d
# !

# Strings can be checked for membership using the 'in' keyword
contains_world = "World" in my_string  # Check if "World" is in the string
print(contains_world)  # Output: True

# Strings can be checked for equality using the '==' operator
is_equal = my_string == "Hello, World!"  # Check if the string is equal to another string
print(is_equal)  # Output: True

# Strings can be compared using relational operators
is_greater = my_string > "Hello, Alice!"  # Compare strings lexicographically
print(is_greater)  # Output: True (because 'W' is greater than 'A')

# Strings can be formatted using the format() method
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)  # Using format method
print(formatted_string2)  # Output: "My name is Alice and I am 30 years old."

# Strings can also be checked for specific prefixes or suffixes
starts_with_hello = my_string.startswith("Hello")  # Check if the string starts with "Hello"
print(starts_with_hello)  # Output: True

ends_with_world = my_string.endswith("World!")
# Check if the string ends with "World!"
print(ends_with_world)  # Output: True

# Strings can be stripped of leading and trailing whitespace using the strip() method
stripped_string = "   Hello, World!   ".strip()  # Remove whitespace from both ends
print(stripped_string)  # Output: "Hello, World!"

# Strings can be checked for alphanumeric characters using the isalnum() method
is_alphanumeric = my_string.isalnum()  # Check if the string contains only alphanumeric characters
print(is_alphanumeric)  # Output: False (because of the space and punctuation)

# Strings can be converted to a list of characters using the list() function
char_list = list(my_string)  # Convert string to a list of characters
print(char_list)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']   

# Strings can be repeated using the '*' operator
repeated_string = my_string * 3  # Repeat the string three times
print(repeated_string)  # Output: "Hello, World!Hello, World!Hello, World!"

# lower() and upper() methods
print(my_string.lower())  # Output: "hello, world!"
print(my_string.upper())  # Output: "HELLO, WORLD!"

# strip() method
whitespace_string = "   Hello, World!   "
print(whitespace_string.strip())  # Output: "Hello, World!"

# replace() method
replaced_string = my_string.replace("World", "Python")
print(replaced_string)  # Output: "Hello, Python!"

# find() method
index_of_world = my_string.find("World")
print(index_of_world)  # Output: 7 (index where "World" starts)

# count() method
count_of_l = my_string.count("l")
print(count_of_l)  # Output: 3 (number of times 'l' appears in the string)

# join() method
words_list = ["Hello", "World"]
joined_string2 = " ".join(words_list)
print(joined_string2)  # Output: "Hello World"

# split() method
split_string = my_string.split(", ")
print(split_string)  # Output: ['Hello', 'World!']

# Order formatting
order_string = "My name is {0} and I am {1} years old.".format(name, age)
print(order_string)  # Output: "My name is Alice and I am 30 years old."


# Join method with a list of strings
# Example of using join() method with a list of strings
string_list = ["apple", "banana", "cherry"]
# Join the list into a single string with commas
joined_string3 = ", ".join(string_list)
print(joined_string3)  # Output: "apple, banana, cherry"



# --- IGNORE ---