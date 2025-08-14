#Transportation Mode Selection
# This code selects a mode of transportation based on the distance to travel.

# <3 km: Walk
# 3-15 km: Bike
# >15 km: Car

# Input: Distance in kilometers

distance = float(input("Enter the distance to travel in kilometers: "))
try:
    if distance < 3:
        print("Suggested mode of transportation: Walk.")
    elif 3 <= distance <= 15:
        print("Suggested mode of transportation: Bike.")
    elif distance > 15:
        print("Suggested mode of transportation: Car.")
    else:
        print("Invalid input. Please enter a valid distance.")
except Exception as e:
    print(f"An error occurred: {e}")

# ############################################################### #
