# Movie Ticket Pricing
# Write a program that determines the price of a movie ticket based on the age of the customer.
# - Child (0-12 years): $5
# - Teenager (13-19 years): $8
# - Adult (20-59 years): $10
# - Senior (60 years and above): $6

age = input("Enter your age: ")
try:
    age = int(age)
    if age < 0:
        print("Invalid age")
    elif age <= 12:
        print("Ticket price: $5 (Child)")
    elif age <= 19:
        print("Ticket price: $8 (Teenager)")
    elif age <= 59:
        print("Ticket price: $10 (Adult)")
    else:
        print("Ticket price: $6 (Senior)")
except ValueError:
    print("Please enter a valid integer for age.")

# ############################################################### #
