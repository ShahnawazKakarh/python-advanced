# Reverse a String using a Loop

def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage:
input_string = "swiss"
result = reverse_string(input_string)
print(f"The reversed string is: {result}")

# ######################################################