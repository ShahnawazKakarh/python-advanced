# Tuple in Python
# Tuples are immutable sequences in Python, used to store a collection of items.
# They are similar to lists but cannot be modified after creation.
# Example:
# A tuple can contain mixed data types, including integers, strings, and
# other objects.
my_tuple = (1, 2, 3, 'apple', 'banana')

# You can access elements in a tuple using indexing, just like lists.
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: apple

# ############################################################### #

# You cannot modify a tuple, but you can create a new tuple based on an
# existing one.
new_tuple = my_tuple + (4, 5)  # Adding new elements creates a new tuple
print(new_tuple)  # Output: (1, 2, 3, 'apple', 'banana', 4, 5)


# ############################################################### #
# How to call a tuple
# You can call a tuple by its name, and it will return the entire tuple.
# Example of a tuple containing fruit names
fruit_tuple = ('apple', 'banana', 'cherry')

print(len(fruit_tuple))  # Output: 3 (the number of items in the tuple)
print(type(fruit_tuple))  # Output: <class 'tuple'>

print(fruit_tuple)  # Output: ('apple', 'banana', 'cherry')
print(fruit_tuple[1])  # Output: banana
print(fruit_tuple[-1])  # Output: cherry (negative indexing)

# ############################################################### #
# Check in a tuple
# You can check if an item exists in a tuple using the 'in' keyword.
