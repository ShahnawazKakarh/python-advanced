# This script demonstrates Python variable scopes

x = "global x"  # This is a global variable

def test():
    y = "local y"  # This is a local variable
    print(x)       # Accessing the global variable
    print(y)       # Accessing the local variable

test()
# print(y)  # This would raise an error because y is not defined in the global scope

