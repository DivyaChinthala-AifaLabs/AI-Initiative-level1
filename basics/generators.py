# generators are used to create iterators
# using yield we can create a generator function
# when next() is called on an iterator, execution runs until it reaches a yield statement.
# generator pauses at yield and remembers its state.
# when next() is called again, execution resumes from where it previously paused.
# in loops, internally it calls iterator object with next method, which returns one value at a time 
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
gen = reverse([1,2,3,4]) # it creates an iterator
print(next(gen))
print(next(gen))

# using generator expressions we can create generators
squares = (x * x for x in range(5))