# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def value_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

value_kwargs(name="Shahnawaz", power="IronMan")
value_kwargs(name="Shahnawaz")
value_kwargs(name="Shahnawaz", power="IronMan", enemy = "Dr. Jackaal")

###############################################################