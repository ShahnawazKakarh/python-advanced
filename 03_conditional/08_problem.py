#Password Strength Checker
#Problem:
# Check if a password is 
# - Weak : < 6 chars
# - Medium : 6-10 chars
# - Strong : >10 chars

password = input("Enter your password: ")
try:
    password_length = len(password)
    
    if password_length < 6:
        print("Your password is weak.")
    elif 6 <= password_length <= 10:
        print("Your password is medium strength.")
    elif password_length > 10:
        print("Your password is strong.")
    else:
        print("Invalid input. Please enter a valid password.")
except Exception as e:
    print(f"An error occurred: {e}")

# ############################################################### #