# Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe, or unripe based on its color.
# - Green: Unripe
# - Yellow: Ripe
# - Brown: Overripe

fruit = input("Enter the color of the fruit (green, yellow, brown): ")
try:
    fruit = fruit.lower()
    if fruit == "green":
        print("The fruit is unripe.")
    elif fruit == "yellow":
        print("The fruit is ripe.")
    elif fruit == "brown":
        print("The fruit is overripe.")
    else:
        print("Invalid color. Please enter green, yellow, or brown.")
except Exception as e:
    print(f"An error occurred: {e}")

# ############################################################### #
