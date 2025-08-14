# Sum of Even Numbers
# This code calculates the sum of all even numbers up to a given number n.
n = 10  # You can change this value to any positive integer
even_sum = 0

for number in range(2, n + 1, 2):  # Start from 2, go up to n, step by 2
    even_sum += number

print("Sum of even numbers up to {}: {}".format(n, even_sum))

# ############################################################### #