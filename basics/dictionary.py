d = {'a': 'Apple', 'b': 'Bat', 'c': 'Cat'}
d['d'] = 'Dog'
print(d['e']) # give keyError when key not exists
d.get('e')
list(d) # give list of keys in the dictionary
'b' in d # check if given key exist in dictionary
dict([(1, 'hello'), (2, 'hi'), (3, 'hmm')]) # dictionary can be created using sequence of key value pairs
{x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}
dict(sape=4139, guido=4127, jack=4098) # {'sape': 4139, 'guido': 4127, 'jack': 4098}
d.items() # returns list of key value pairs in dictionary
