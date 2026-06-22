# Exceptions are used to handle the errors while executing the python program, without stopping the program
try:
    a = int(input("Enter some number:"))
    print(a)
except Exception as e:
    print(f'Error occurred {e}')
else:
    print(f"Exceute when no exception occurred")
finally:
    print('It excecute everytime')


# raise exception
age = 5
try:
    if(age > 0):
        print('Valid age entered')
        raise ValueError('Invalid age entered')
except ValueError as e:
    print(f'Error: {e}')

    
# use meaningful exceptions whenever possible
# use finally for cleanup

# try:
#     # risky code
# except SpecificError as e:
#     # handle error
# else:
#     # success path
# finally:
#     # cleanup

# custom exception
class InvalidAgeError(Exception):
    pass

age = -4
if(age < 0):
    raise InvalidAgeError("Invali age entered")