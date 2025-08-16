# Find the First Non-Repeated Character
# Given a string, find the first non-repeated character

def first_non_repeated_char(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    for char in input_string:
        if char_count[char] == 1:
            return char
    return None

# Example usage:
input_str = "swiss"
result = first_non_repeated_char(input_str)
print(f"The first non-repeated character is: {result}")

# ######################################################