from datetime import datetime

# Movie Ticket Pricing
# Write a program that determines the price of a movie ticket based on the age of the customer.
# - children (below 18): $8
# - Adults ((18 and over)): $12
# - Everyone gets a $2 discount on Wednesdays.

# < less than, > greater than, <= less than or equal to, >= greater than or equal to
# Note: The day of the week is represented as an integer where Monday is 0 and Sunday is 6.

age = input("Enter your age: ")

try:
    age = int(age)
    today = datetime.now().weekday()
    if age < 0:
        print("Invalid age")
    elif age < 18 and today == 2: 
        print("Ticket price: $6 (Children with discount)")
    elif age < 18 and not today == 2:
        print("Ticket price: $8 (Children)")
    elif age >= 18 and today == 2:
        print("Ticket price: $10 (Adults with discount)")
    else:
        print("Ticket price: $12 (Adults)")

except ValueError:
    print("Please enter a valid integer for age.")

# ############################################################### #
