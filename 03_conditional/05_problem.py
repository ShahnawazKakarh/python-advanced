#Weather Activity Suggestion
# Problem: Suggest an activity based on the weather
# - Sunny: Go for a walk
# - Rainy: Read a book
# - Snowy: Build a snowman

weather = input("Enter the weather (sunny, rainy, snowy): ")
try:
    weather = weather.lower()
    if weather == "sunny":
        print("Suggested activity: Go for a walk.")
    elif weather == "rainy":
        print("Suggested activity: Read a book.")
    elif weather == "snowy":
        print("Suggested activity: Build a snowman.")
    else:
        print("Invalid input. Please enter sunny, rainy, or snowy.")
except Exception as e:
    print(f"An error occurred: {e}")

# ############################################################### #