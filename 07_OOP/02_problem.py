# Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# Basic Class and Object
# Problem: Create a Car class with attributes/variables like brand and model.
# Then create an instance of this class.
# __init__ is also called instructor
# self is helping to connect class with it methods
# Defining a class named Car
class Car:
    # __init__ is a special method (called a constructor)
    # It automatically runs when you create a new object of this class.
    # 'self' refers to the current object being created/used.
    def __init__(self, brand, model):
        # Assign the parameter 'brand' to the object's 'brand' property
        self.brand = brand
        # Assign the parameter 'model' to the object's 'model' property
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Creating an instance (object) of Car class
# Here, 'my_car' becomes a Car object with brand="Toyota", model="Corolla"
my_car = Car("Toyota", "Corolla")

# Accessing the object's properties using dot notation
print(my_car.brand)   # Output: Toyota
print(my_car.model)   # Output: Corolla
print(my_car.full_name())    # Output: Toyota Corolla


# Reassigning 'my_car' to a new Car object with different values
# This creates a new Car object (brand="Honda", model="Civic")
my_car2 = Car("Honda", "Civic")

# Now 'my_car' points to this new object, not the previous Toyota one
print(my_car2.brand)   # Output: Civic
