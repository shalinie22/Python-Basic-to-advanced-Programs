# 7. Employee Salary

# Create an Employee class.

# Attributes

# name
# basic_salary

# calculate_salary()

# Gross = Basic + 20% HRA + 10% Bonus

class Employee:

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary * 1.30

E1 = Employee("Shalinie", 70000)

print(E1.calculate_salary())