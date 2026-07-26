# 9. Method Overriding

# Create

# Animal

# Method

# sound()

# Child classes

# Dog
# Cat
# Cow

# Each overrides sound().

# Output

# Dog says Bark

# Cat says Meow

# Cow says Moo

class Animal:
    def sound(self):
        return "Animal sounds"

class Dog(Animal):

    def sound(self):
        return "Dog says Bark"

class Cat(Animal):

    def sound(self):
        return "Cat says Meow"

class Cow(Animal):

    def sound(self):
        return "Cow says Moo"

D1 = Dog()
C1 = Cat()
M1 = Cow()

print(D1.sound())
print(C1.sound())
print(M1.sound())



