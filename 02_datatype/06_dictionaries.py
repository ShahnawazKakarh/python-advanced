# Dictionarys are mutable mappings in Python, used to store key-value pairs.
# They allow for fast retrieval of values based on unique keys.
# Example:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# You can access values in a dictionary using their keys.
print(my_dict['name'])  # Output: Alice

# ############################################################### #

# You can also add new key-value pairs or modify existing ones.
my_dict['age'] = 31  # Modifying the value for the key 'age'
my_dict['country'] = 'USA'  # Adding a new key-value pair
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
print(my_dict)


# ############################################################### #
# How to call a dictionary
# You can call a dictionary by its name, and it will return the entire
# dictionary.
tea_list = ['Green Tea', 'Black Tea', 'Herbal Tea',
            'Masala Tea']  # Example of a list containing strings
tea_types = {'black': 'strong and bold',
             'green': 'light and refreshing',
             'herbal': 'caffeine-free and soothing'
             }  # Example of a dictionary containing tea types and their descriptions

print(len(tea_list))  # Output: 4 (the number of items in the list)
# Output: 3 (the number of key-value pairs in the dictionary)
print(len(tea_types))
print(type(tea_list))  # Output: <class 'list'>
print(type(tea_types))  # Output: <class 'dict'>

# Output: ['Green Tea', 'Black Tea', 'Herbal Tea', 'Masala Tea']
print(tea_list)
# Output: {'black': 'strong and bold', 'green': 'light and refreshing', 'herbal': 'caffeine-free and soothing'}
print(tea_types)
print(tea_types['green'])  # Output: light and refreshing
print(tea_types.get('black'))  # Output: strong and bold

# ############################################################### #
# Check in a dictionary
# You can check if a key exists in a dictionary using the 'in' keyword.
if 'green' in tea_types:
    print("Green tea is available.")  # Output: Green tea is available.
else:
    print("Green tea is not available.")

# You can also check if a value exists in a dictionary using the 'in' keyword.
if 'caffeine-free and soothing' in tea_types.values():
    # Output: A caffeine-free tea is available.
    print("A caffeine-free tea is available.")
else:
    print("No caffeine-free tea available.")

# For loop in a dictionary
# You can iterate over the keys, values, or key-value pairs in a
# dictionary using a for loop.
for key in tea_types:
    # Output: black: strong and bold, green: light and refreshing, herbal:
    # caffeine-free and soothing
    print(key, ":", tea_types[key])


# You can also use the items() method to iterate over key-value pairs.
for key, value in tea_types.items():
    # Output: black -> strong and bold, green -> light and refreshing, herbal
    # -> caffeine-free and soothing
    print(key, "->", value)
# You can use the keys() method to iterate over keys.
for key in tea_types.keys():
    print("Key:", key)  # Output: Key: black, Key: green, Key: herbal
# You can use the values() method to iterate over values.
for value in tea_types.values():
    # Output: Value: strong and bold, Value: light and refreshing, Value:
    # caffeine-free and soothing
    print("Value:", value)
# You can also use a for loop to iterate over a list of dictionaries.
tea_list = [
    {'name': 'Green Tea', 'type': 'green', 'caffeine': False},
    {'name': 'Black Tea', 'type': 'black', 'caffeine': True},
    {'name': 'Herbal Tea', 'type': 'herbal', 'caffeine': False}
]

for tea in tea_list:
    print(
        tea['name'],
        "is a",
        tea['type'],
        "tea with caffeine:",
        tea['caffeine'])
# Output: Green Tea is a green tea with caffeine: False
#         Black Tea is a black tea with caffeine: True
#         Herbal Tea is a herbal tea with caffeine: False

# ############################################################### #
# How to add, update, and remove items in a dictionary

tea_types.add('oolong', 'smooth and rich')  # Adding a new key-value pair
# Output: {'black': 'strong and bold', 'green': 'light and refreshing', 'herbal': 'caffeine-free and soothing', 'oolong': 'smooth and rich'}
print(tea_types)

# Updating the dictionary with a new key-value pair
tea_types.update({'white': 'delicate and floral'})
# Output: {'black': 'strong and bold', 'green': 'light and refreshing', 'herbal': 'caffeine-free and soothing', 'oolong': 'smooth and rich', 'white': 'delicate and floral'}
print(tea_types)

tea_types.pop('herbal')  # Removing a key-value pair
# Output: {'black': 'strong and bold', 'green': 'light and refreshing', 'oolong': 'smooth and rich', 'white': 'delicate and floral'}
print(tea_types)

tea_types.popitem()  # Removing the last inserted key-value pair
# Output: {'black': 'strong and bold', 'green': 'light and refreshing', 'oolong': 'smooth and rich'}
print(tea_types)

# Updating the value for the key 'black'
tea_types["black"] = 'strong and bold with a hint of smokiness'
# Output: {'black': 'strong and bold with a hint of smokiness', 'green': 'light and refreshing', 'oolong': 'smooth and rich'}
print(tea_types)

del tea_types['green']  # Deleting the key 'green' from the dictionary
# Output: {'black': 'strong and bold with a hint of smokiness', 'oolong': 'smooth and rich'}
print(tea_types)


# ############################################################### #
# Example of a dictionary representing a tea shop
tea_shop = {
    'name': 'The Tea House',
    'location': 'Downtown',
    'menu': {
        'black_tea': {'price': 2.5, 'caffeine': True},
        'green_tea': {'price': 2.0, 'caffeine': False},
        'herbal_tea': {'price': 3.0, 'caffeine': False}
    },
    'ratings': [4.5, 4.0, 5.0]
}  # Example of a dictionary representing a tea shop


# You can access the tea shop's name and location.
print(tea_shop['name'])  # Output: The Tea House
print(tea_shop['location'])  # Output: Downtown

# You can access the menu and its items.
print(tea_shop['menu']['black_tea']['price'])  # Output: 2.5
print(tea_shop['menu']['green_tea']['caffeine'])  # Output: False

# You can also access the ratings of the tea shop.
print(tea_shop['ratings'])  # Output: [4.5, 4.0, 5.0]
# Output: Average rating: 4.5
print("Average rating:", sum(tea_shop['ratings']) / len(tea_shop['ratings']))

# ############################################################### #

# Copying a dictionary
# Copied to use it later
tea_types_copy = tea_types.copy()  # Creating a shallow copy of the dictionary
# Output: {'black': 'strong and bold with a hint of smokiness', 'oolong': 'smooth and rich'}
print(tea_types_copy)


# ############################################################### #
# Dictionary in a dictionary
# You can have dictionaries within dictionaries, allowing for complex data
# structures.
nested_dict = {
    'tea': {
        'black': {'caffeine': True, 'flavor': 'strong'},
        'green': {'caffeine': False, 'flavor': 'light'},
        'herbal': {'caffeine': False, 'flavor': 'soothing'}
    }
}  # Example of a nested dictionary

# You can access nested dictionaries using multiple keys.
print(nested_dict['tea']['black']['caffeine'])  # Output: True
print(nested_dict['tea']['green']['flavor'])  # Output: light

# dictionaries can also be used to represent more complex data structures, such as JSON-like objects.
# For example, you can represent a person's information as a dictionary.
person_info = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA'
    },
    'hobbies': ['reading', 'traveling', 'cooking']
}

# You can access nested information in the person_info dictionary.
print(person_info['name'])  # Output: John Doe
print(person_info['address']['city'])  # Output: Anytown
print(person_info['hobbies'][1])  # Output: traveling

# ############################################################### #

# Dictionary comprehension
# You can create dictionaries using dictionary comprehension, which is a
# concise way to generate dictionaries.
squares = {x: x**2 for x in range(1, 6)}  # Creating a dictionary of squares
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# You can also filter items while creating a dictionary.
# Creating a dictionary of squares of even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# ############################################################### #
# Merging dictionaries
# You can merge two dictionaries using the update() method or the |
# operator in Python 3.9+.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)  # Merging dict2 into dict1
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Alternatively, you can use the | operator to merge dictionaries.
merged_dict = dict1 | dict2  # Merging dict1 and dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# dict.fromkeys() method
# You can create a new dictionary with specified keys and a default value
# using the fromkeys() method.
keys = ['a', 'b', 'c']
default_value = 0
# Creating a dictionary with keys and a default value
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# ############################################################### #
