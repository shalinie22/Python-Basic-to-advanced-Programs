# 8. Inheritance

# Create

# Vehicle

# ↓

# Car

# Vehicle contains

# brand
# model

# Car additionally contains

# fuel_type

# Print all details using inherited methods.


class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):

    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)   # Call Vehicle constructor
        self.fuel_type = fuel_type


# Create Car object
c1 = Car("Porsche", "P1", "Petrol")

print("Brand:", c1.brand)
print("Model:", c1.model)
print("Fuel Type:", c1.fuel_type)