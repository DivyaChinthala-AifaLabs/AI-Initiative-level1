# function arguments
# these are passed when calling the function

def myName(firstName, lastName="Ch"):
    print(f"Hello {firstName} {lastName}")

# positional arguments
myName("Divya", "Chinthala")

# keyword arguments
# specify parameter names when calling the function
myName(lastName= "Chinthala", firstName= "Divya")

# default arguments
myName("Divya")

# variable length positional arguments
def sum(*args):
    print(args)
    print(type(args))
sum(1,2,3,4,5)

# variable length keyword arguments
def sum(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(f"{kwargs['name']}'s role is {kwargs['role']}")
sum(name="Divya", role="developer")

# unpacking arguments
def add(a,b):
    print(a+b)
nums=[1,2]
add(*nums)

def getUser(name, role):
    print(f"Name: {name}, Role: {role}")
user={"name": "Divya", "role": "Developer"}
getUser(**user)

# pass by value
def num(a):
    a = 10
    print(a)
x = 5
num(x)
print(x)

# pass by reference
def obj(list):
    list.append(5)
li = [1,2,3]
obj(li)
print(li)
