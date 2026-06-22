# sequences & tuples
s = 1234, 123, 'divya'
print(s)
print(s[0]) # accessing a tuple element

t = s, 'hello', (1,2,3,4) # creating tuple inside a tuple
print(t)

t1 = (123,) # to create a tuple with single item
t1 = t1 + (1234,) # to add new elements to tuple, we can only concatenate a tuple
x,y = t1