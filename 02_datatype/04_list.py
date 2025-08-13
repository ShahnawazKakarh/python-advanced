# Accessing and manipulating lists in Python
# Lists are mutable sequences, typically used to store collections of items.

my_list = [1, 2, 3, 4, 5]  # Example of a list 
# Lists can contain elements of different data types, including numbers, strings, and other lists.
# You can access elements in a list using indexing, similar to strings.

# Get first element of the list
first_element = my_list[0]  # Accessing the first element
print(first_element)  # Output: 1

# Get a sublist from the list
sublist = my_list[1:4]  # Accessing a sublist from index 1 to 3
print(sublist)  # Output: [2, 3, 4]

# Practice
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Example of a list containing numbers
# Get the first element of num_list
first_num = num_list[0]  # Accessing the first element
print(first_num)  # Output: 0

one_to_five = num_list[1:5]  # Get a sublist from index 1 to 4
print(one_to_five)  # Output: [1, 2, 3, 4]

entire_list = num_list[:]  # Get the entire list
print(entire_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_seven = num_list[:7]  # Get the first seven elements of the list
print(first_seven)  # Output: [0, 1, 2, 3, 4, 5, 6] 


# ############################################################### #

num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']  # Example of a list containing strings

# You can access elements in a list using negative indexing, which counts from the end of the list.
last_element = num_list[-1]  # Accessing the last element
print(last_element)  # Output: 'nine'

# You can also access a range of elements using slicing.
last_three_elements = num_list[-3:]  # Accessing the last three elements
print(last_three_elements)  # Output: ['eight', 'nine']

slicing_second_num = num_list[1:2] = "Lemon" # Slicing to get the second element and replace it with "Lemon"
print(slicing_second_num)  # Output: ['zero', 'Lemon', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num_list[1:3] # Slicing to get the second and third elements
print(num_list[1:3])  # Output: ['Lemon', 'two']


num_list[1:3] = ['Orange'] # Replacing the second and third elements with 'Orange'
print(num_list)  # Output: ['zero', 'Orange', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print("Slicing with empty range:")
# Slicing with an empty range will return an empty list.
empty_slice = num_list[1:1]
print(empty_slice)  # Output: [] (an empty list, since no elements are selected)

print("Adding multiple elements to a slice:")
# You can also replace a slice of elements with multiple new elements.
num_list[1:2] = ['test', 'test'] # Replacing the second element with two new elements 'test'
print(num_list)  # Output: ['zero', 'test', 'test', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


# ############################################################### #

# Lists are mutable, meaning you can change their content after creation.
# For example, you can change an element in the list.
my_list[0] = 10  # Changing the first element
print(my_list)  # Output: [10, 2, 3, 4, 5]

# ############################################################### #

tea_list = ['Green Tea', 'Black Tea', 'Herbal Tea', 'Masala Tea']  # Example of a list containing strings
for tea in tea_list:
    print(tea)  # Prints each type of tea in the list

for tea in tea_list:
    print(tea, end='-')

if 'Green Tea' in tea_list:  # Checking if 'Green Tea' is in the list
    print("\nGreen Tea is available!")  # Output: Green Tea is available!
else:
    print("\nGreen Tea is not available.") and tea_list.append('Green Tea')  # Adding 'Green Tea' to the list if not present

tea_list.append('Oolong Tea')  # Appending 'Oolong Tea' to the list
print(tea_list)  # Output: ['Green Tea', 'Black Tea', 'Herbal Tea', 'Masala Tea', 'Oolong Tea']

tea_list.remove('Black Tea')  # Removing 'Black Tea' from the list
print(tea_list)  # Output: ['Green Tea', 'Herbal Tea', 'Masala Tea', 'Oolong Tea']

tea_list.pop(2)  # Popping the element at index 2 (which is 'Masala Tea')
print(tea_list)  # Output: ['Green Tea', 'Herbal Tea', 'Oolong Tea']


# ############################################################### #

# You can also append new elements to the list using the append() method.
my_list.append(6)  # Appending a new element
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Lists can be concatenated using the '+' operator
another_list = [7, 8, 9]
combined_list = my_list + another_list  # Concatenation
print(combined_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# You can also use the extend() method to add multiple elements from another iterable.
my_list.extend([11, 12])  # Extending the list with new elements
print(my_list)  # Output: [10, 2, 3, 4, 5, 6, 11, 12]

# Lists support various methods for manipulation, such as sort(), reverse(), pop(), remove(), etc.
my_list.sort()  # Sorting the list
print(my_list)  # Output: [2, 3, 4, 5, 6, 10, 11, 12]

my_list.reverse()  # Reversing the list
print(my_list)  # Output: [12, 11, 10, 6, 5, 4, 3, 2]

# You can remove an element from the list using the remove() method.
my_list.remove(10)  # Removing the element 10
print(my_list)  # Output: [12, 11, 6, 5, 4, 3, 2]

# You can also pop an element from the list, which removes it and returns the value.
popped_element = my_list.pop()  # Popping the last element
print(popped_element)  # Output: 2
print(my_list)  # Output: [12, 11, 6, 5, 4, 3]

# Lists can contain other lists, allowing for nested structures.
nested_list = [1, 2, [3, 4], 5]  # Example of a nested list
print(nested_list[2])  # Output: [3, 4]
print(nested_list[2][0])  # Accessing an element in the nested list, Output: 3  


# You can also use list comprehensions for creating lists in a concise way.
squared_numbers = [x**2 for x in range(10)]  # Creating a list of squared numbers
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehensions can also include conditions.
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Squaring only even numbers
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Lists can be sliced similarly to strings, allowing you to access a range of elements.
sliced_list = my_list[1:4]  # Slicing the list from index 1 to 3
print(sliced_list)  # Output: [11, 6, 5]

# You can also use the len() function to get the number of elements in a list.
list_length = len(my_list)  # Getting the length of the list
print(list_length)  # Output: 6 (after previous modifications)

# Lists can be iterated over using loops.
for item in my_list:
    print(item)  # Prints each item in the list

# You can also check if an element exists in a list using the 'in' keyword.
contains_five = 5 in my_list  # Check if 5 is in the list
print(contains_five)  # Output: True


# You can find the length of a list using the len() function
list_length = len(my_list)  # Get the length of the list
print(list_length)  # Output: 6 (after previous modifications)

# Lists can be indexed and sliced like strings
first_item = my_list[0]  # Get the first item
print(first_item)  # Output: 12

sublist = my_list[1:4]  # Get a sublist from index 1 to 3
print(sublist)  # Output: [11, 6, 5]

# Lists can also be iterated over in a loop
for item in my_list:
    print(item, end=' ')  # Print each item in the list
# Output: 12 11 6 5 4 3 
print()  # New line after the loop

# Another example of list iteration in loop without end parameter
for item in my_list:
    print(item)  # Print each item on a new line
# Output:
# 12
# 11
# 6
# 5
# 4
# 3
# Lists can be checked for membership using the 'in' keyword
contains_six = 6 in my_list  # Check if 6 is in the list
print(contains_six)  # Output: True

# Lists can be checked for equality using the '==' operator
is_equal_list = my_list == [12, 11, 6, 5, 4, 3]  # Check if the list is equal to another list
print(is_equal_list)  # Output: True

# Lists can be compared using relational operators
is_greater_list = my_list > [10, 9, 8]  # Compare lists lexicographically
print(is_greater_list)  # Output: True (because the first element 12 is greater than 10)

# Lists can also be nested, meaning a list can contain other lists as elements.
nested_list = [[1, 2], [3, 4], [5, 6]]  # Example of a nested list
print(nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]

# You can access elements in a nested list using multiple indices.
first_nested_element = nested_list[0][1]  # Accessing the second element of the first nested list
print(first_nested_element)  # Output: 2

# You can also flatten a nested list using list comprehensions.
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

# Lists can be used to store mixed data types, including strings, numbers, and other lists.
mixed_list = [1, "Hello", 3.14, [5, 6]]
print(mixed_list)  # Output: [1, 'Hello', 3.14, [5, 6]]
# You can access elements in a mixed list just like any other list.
print(mixed_list[1])  # Output: "Hello"

# You can also use the 'del' statement to remove an element from a list by its index.
del my_list[0]
print(my_list)  # Output: [11, 6, 5, 4, 3] (after deleting the first element)

# Lists can be sorted using the sort() method, which sorts the list in place.
my_list.sort()
print(my_list)  # Output: [3, 4, 5, 6, 11] (after sorting)
# You can also use the sorted() function to return a new sorted list without modifying the original.
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [3, 4, 5, 6, 11] (sorted version of my_list)

# Lists can be formatted using the format() method, similar to strings.
formatted_list = "List elements: {}".format(my_list)
print(formatted_list)  # Output: "List elements: [3, 4, 5, 6, 11]"

# Lists can also be formatted using f-strings (Python 3.6+).
f_formatted_list = f"List elements: {my_list}"
print(f_formatted_list)  # Output: "List elements: [3, 4, 5, 6, 11]"


# Lists can be used in various data structures, such as stacks and queues.
# For example, you can use the append() method to add elements to the end of a list (like a stack).
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
print(stack)  # Output: [1, 2]

# You can use the pop() method to remove elements from the end of the list (like a stack).
popped_element = stack.pop()
print(popped_element)  # Output: 2 (the last element popped from the stack)
print(stack)  # Output: [1] (after popping)

# Lists can also be used as queues by using the pop(0) method to remove elements from the front.
queue = []
queue.append(1)  # Enqueue 1
queue.append(2)  # Enqueue 2
print(queue)  # Output: [1, 2]

dequeued_element = queue.pop(0)  # Dequeue the first element
print(dequeued_element)  # Output: 1 (the first element dequeued from the queue)
print(queue)  # Output: [2] (after dequeuing)