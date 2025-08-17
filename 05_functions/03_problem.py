# Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# It means there’s a function called multiply that can handle two kinds of inputs:
# If you give it numbers, it returns their product (e.g., 3 and 4 → 12).
# If you give it text (a string), it treats “multiply” as repeat the text a certain number of times (e.g., “hi” and 3 → “hihihi”).
# So the same function works for both numbers and strings, depending on what you pass in.

def multiple_of_two_numbers(a, b):
    if type(a) == int and type(b) == int:
        return a * b
    elif type(a) == str and type(b) == int:
        return a * b
    elif type(a) == int and type(b) == str:
        return b * a
    else:
        raise TypeError("Unsupported types: use (int, int) or (str, int)")

# ✅ Valid cases
print(multiple_of_two_numbers(3, 4))      # 12
print(multiple_of_two_numbers("hi", 3))   # hihihi
print(multiple_of_two_numbers(3, "hi"))   # hihihi

# ❌ Invalid case
print(multiple_of_two_numbers("hi", "hi"))  # Raises TypeError

# ############################################################### #