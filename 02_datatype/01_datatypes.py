# --- Understanding of Mutable and Immutable ---
# Mutable objects can be changed after they are created (e.g., lists, dictionaries, sets).
# Immutable objects cannot be changed after they are created (e.g., strings, tuples, integers).
# Example:
my_list = [1, 2, 3] # mutable
my_tuple = (1, 2, 3) # immutable

my_list.append(4) # modifies the original list
print("Modified List:", my_list)

# my_tuple[0] = 4 # This will raise an error because tuples are immutable
print("Tuple:", my_tuple)
# --- IGNORE ---

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



# --- Copy, DeepCopy in Python ---
import copy

original_list = [1, 2, 3]
# shallow_copy = Copy the list
# deep_copy = Copy the list and its further lists/elements
# Shallow copy and deep copy are two ways to duplicate objects in Python.
# Shallow copy creates a new object, but inserts references into it to the objects found in the original.
# Deep copy creates a new object and recursively adds copies of nested objects found in the original.

# Using copy and deepcopy from the copy module
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

original_list.append(4)
shallow_copy.append(5)
deep_copy.append(6)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
# --- IGNORE ---

# --- Copy with respect to Slicing ---
original_list = [1, 2, 3]
shallow_copy = original_list[:]

original_list.append(4)
shallow_copy.append(5)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
# --- IGNORE ---

# --- Understanding of `is` and `==` ---
# `is` checks for reference identity (whether two references point to the same object in memory)
# `==` checks for value equality (whether the values of two objects are the same)
# Example:
n = [1, 2, 3]
m = n
print(n)
print(m)
print(n == m) # true because their values are the same
print(n is m) # true because they point to the same object in memory

m = [1, 2, 3]
print(n == m) # true because their values are the same
print(n is m) # false because they are different objects in memory
# --- IGNORE ---
