#Coffee Customization
# Problem: Customize a Coffee Order
# - Small: Regular coffee
# - Medium: Regular coffee with an extra shot of espresso
# - Large: Regular coffee with two extra shots of espresso

coffee_size = input("Enter the coffee size (small, medium, large): ")
extra_shot = input("Would you like an extra shot of espresso? (yes/no): ")

try:
    coffee_size = coffee_size.lower()
    extra_shot = extra_shot.lower()
    
    if coffee_size == "small":
        print("Your order: Regular coffee.")
    elif coffee_size == "medium":
        if extra_shot == "yes":
            print("Your order: Regular coffee with an extra shot.")
        else:
            print("Your order: Regular coffee.")
    elif coffee_size == "large":
        if extra_shot == "yes":
            print("Your order: Regular coffee with two extra shots.")
        else:
            print("Your order: Regular coffee with one extra shot.")
    else:
        print("Invalid input. Please enter small, medium, or large for coffee size.")
except Exception as e:
    print(f"An error occurred: {e}")
# ############################################################### #

