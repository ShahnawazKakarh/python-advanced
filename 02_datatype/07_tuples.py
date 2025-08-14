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
print(fruit_tuple[0:2])  # Output: ('apple', 'banana') (slicing)
print(fruit_tuple[1:])  # Output: ('banana', 'cherry') (slicing from index 1)
print(fruit_tuple[:2])  # Output: ('apple', 'banana') (slicing up to index 2)
print(fruit_tuple[::2])  # Output: ('apple', 'cherry') (slicing with step)
# Output: ('cherry', 'banana', 'apple') (reversed tuple)
print(fruit_tuple[::-1])
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
# (repeating the tuple)
print(fruit_tuple * 2)

# ############################################################### #
# Check in a tuple
# You can check if an item exists in a tuple using the 'in' keyword.
print('banana' in fruit_tuple)  # Output: True
print('orange' in fruit_tuple)  # Output: False

# ############################################################### #

# Tuple unpacking
# You can unpack the elements of a tuple into separate variables.
a, b, c = fruit_tuple
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry

# ############################################################### #

# Cancatenating tuples
# You can concatenate two or more tuples to create a new tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# ############################################################### #

# Tuple methods
# Tuples have a few built-in methods, such as count() and index().
# count() returns the number of occurrences of a specified value.
# index() returns the index of the first occurrence of a specified value.
example_tuple = (1, 2, 3, 2, 4)
print(example_tuple.count(2))  # Output: 2 (count of 2 in the tuple)
print(example_tuple.index(3))  # Output: 2 (index of the first occurrence of 3)

# ############################################################### #

# Tuple as a key in a dictionary
# Tuples can be used as keys in dictionaries because they are immutable.
# Example:
my_dict = {
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(my_dict[(1, 2)])  # Output: Point A
print(my_dict[(3, 4)])  # Output: Point B

# ############################################################### #

# Tuple with single element
# To create a tuple with a single element, you need to include a trailing
# comma.
single_element_tuple = (42,)  # This is a tuple with one element
print(single_element_tuple)  # Output: (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# If you don't include the comma, it will be treated as a regular value.
not_a_tuple = (42)  # This is not a tuple, just an integer
print(not_a_tuple)  # Output: 42
print(type(not_a_tuple))  # Output: <class 'int'>

# ############################################################### #

# Counting elements in a tuple
# You can count the number of elements in a tuple using the len() function.
count_tuple = (1, 2, 3, 4, 5)
print(len(count_tuple))  # Output: 5 (the number of elements in the tuple)

# ############################################################### #

# Tuple Unwrapping
# You can unpack a tuple into multiple variables.
unpacked_tuple = (10, 20, 30)
x, y, z = unpacked_tuple
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30
# If the number of variables does not match the number of elements in the tuple,
# it will raise a ValueError.
# Example:
# x, y = unpacked_tuple  # This will raise an error because there are 3
# elements in the tuple.

# ############################################################### #

# Nested tuples
# Tuples can contain other tuples, allowing for complex data structures.
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][1])  # Output: 4 (accessing an element in a nested tuple)

# ############################################################### #
