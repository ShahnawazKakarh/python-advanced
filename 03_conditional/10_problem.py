# Pet Food Recommendation
# Problem:
# Recommend a type of pet food based on the pet's species and age
# Dog: <2 years - Puppy food
# Cat: >5 years - Senior cat food

species = input("Enter your pet's species (dog/cat): ").strip().lower()
age = input("Enter your pet's age in years: ")

try:
    age = float(age)
    
    if species == "dog":
        if age < 2:
            print("Recommend: Puppy food")
        else:
            print("Recommend: Adult dog food")
    elif species == "cat":
        if age > 5:
            print("Recommend: Senior cat food")
        else:
            print("Recommend: Adult cat food")
    else:
        print("Invalid species. Please enter 'dog' or 'cat'.")
except ValueError:
    print("Invalid input for age. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
    
# ############################################################### #
