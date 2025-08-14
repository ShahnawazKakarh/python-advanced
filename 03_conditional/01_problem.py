# Age Group Categorization
# Problem: Write a Python program that categorizes a person's age into different groups:
# - Child: 0-12 years or < 13
# - Teenager: 13-19 years
# - Adult: 20-59 years
# - Senior: 60 years and above

# Enter Age
# If the age is less than 0, print "Invalid age".
# If the age is between 0 and less than 13, print "Child".
# If the age is between 13 and 19, print "Teenager".
# If the age is between 20 and 59, print "Adult".
# If the age is 60 or above, print "Senior".
# User input should be handled to ensure it is a valid integer.
# User can input any age, and the program should categorize it accordingly.
# < less than, > greater than, <= less than or equal to, >= greater than or equal to
# Bonus: Handle invalid input gracefully.


age = input("Enter you age:")
try:
    age = int(age)
    if age < 0:
        print("Invalid age")
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 60:
        print("Adult")
    else:
        print("Senior")

except ValueError:
    print("Please enter a valid integer for age.")

# ############################################################### #
