# 5. Student Class

# Create a class Student with

# name
# age
# marks

# Methods

# display()
# is_pass() (returns True if marks >= 40)


class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

    def is_pass(self):
        if self.marks >= 40:
            return True
        else:
            return False

s1 = Student("Shalinie", 27, 90)

s1.display()
print(s1.is_pass())