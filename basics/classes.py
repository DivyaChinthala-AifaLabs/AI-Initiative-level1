class Person:
    species = 'Human' #shared across all objects
    def __init__(self, name, age): #it is called automatically whe obj is created
        self.name = name
        self.age = age
    def greet(self):
        # species = 'Animals'
        print(f"Hello, I am {self.name}, {self.species}")
    def __str__(self): # when object prints directly, it calls this function without printing memory representation
        return f"Person object - {self.name}"

person1 = Person("John", 29) # this creates an object
print(person1)
print(person1.name)
print(person1.age)
person1.greet()

# inheritance - 
# it is used when child classes wants to use parent class attributes & methods
# To reuse code
# to override the functionality
# super method is used to call parent class contructor
class Employee(Person):
    def __init__(self, name, age, company, role):
        super().__init__(name, age)
        self.role = role;
        self.company = company

    def details(self):
        self.greet()
        print(f'Details: In {self.company}, working as {self.role}')

employee1 = Employee('John', 28, "XYZ", "Full Stack Developer")
print(employee1.details())


# class method
# we can access the method without creating object
class Animal:
    species = "animal"

    @classmethod
    def get_species(cls):
        return cls.species

print(Animal.get_species())


class EmployeeData:
    count = 0
    def __init__(self):
        EmployeeData.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

EmployeeData()
EmployeeData()
print(EmployeeData.get_count())

# static method
# sometimes we want to put related functionality closely in a class
# to create static method, we dont need cls or self
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
    
    def sub(a,b):
        return a - b
    
print(MathUtils.sub(4,3))
    
