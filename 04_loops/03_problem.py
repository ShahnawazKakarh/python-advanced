#Multiplication Table Printer
#Problem:
# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter a number to print its multiplication table: "))
print("Multiplication Table for {}:".format(number))
for i in range(1, 11):
    if i == 5:
        continue  # Skip the fifth iteration
    print("{} x {} = {}".format(number, i, number * i))

# ############################################################### #

# Contine explanation:
# This code prompts the user to enter a number and then prints the multiplication table for that number from 1 to 10,
# skipping the fifth iteration.

# Key part:
# When i == 5, the continue statement tells Python:
# “Skip everything below this point in the current loop iteration and move to the next one.”
# That’s why you don’t see 3 x 5 = 15 in the output.