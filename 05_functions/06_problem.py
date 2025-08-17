# Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

# Usually we do with function but such methods which are not gonna use again can be used via lambda function
def cube(x):
    return x**3
print(cube(3))

# With Lambda Function
cube_of_number = lambda x: (x**3)
print(cube_of_number(3))

# ############################################################### #