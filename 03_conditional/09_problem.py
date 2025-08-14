#Leap Year Checker
#Problem:
# Determine if a year is a leap year.
# Leap years are divisible by 4, but not by 100 unless also divisible by 400.

year = input("Enter a year: ")
try:
    year = int(year)
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
except Exception as e:
    print(f"An error occurred: {e}")

# ############################################################### #
