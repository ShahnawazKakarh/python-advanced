# Sum of Even Numbers
# This code calculates the sum of all even numbers up to a given number n.
n = 10  # You can change this value to any positive integer
even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:  # Check if the number is even
        even_sum += i  # Add the even number to the sum

print("Sum of even numbers up to {}: {}".format(n, even_sum))

# ############################################################### #