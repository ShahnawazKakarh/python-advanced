# Grade Calculator
# This program calculates the grade based on the score input by the user.
# It categorizes the score into different grade bands.

# Problem:
# Assign a letter grade based on a student's score:
# A (90-100)
# B (80-89)
# C (70-79)
# D (60-69)
# F (below 60).

score =input("Enter your score: ")
try:
    score = int(score)
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
except ValueError:
    print("Please enter a valid integer for the score.")

# ############################################################### #