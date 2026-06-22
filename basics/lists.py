li = [1,2,3,4,5]
li.append(6) # add element at end of the list
li.extend([7,8,9]) # add iterable elements to end of the list
li.remove(7) # removes specified element from the list
li.insert(1,10) # insert the given value at give position
li.clear() # remove all elements from the list
li.pop(1) # remove element at certain position and returns the removed element
li.index(2,3,5) # return the index of the given value, take start and last position to search
li.count(2) # returns number of times the value is there in the list
li.sort(True) # sorts the list
li.reverse() # reverse the list elements
li.copy() # copies the list

# del is used to delete the element using index
# del li[1]
# del li - deletes entire li variable
enumerate(li) # returns the index and value
zip(li, [1,2,3,4], ['a','b','c','d']) # loop over two or more sequences, entires can be paired