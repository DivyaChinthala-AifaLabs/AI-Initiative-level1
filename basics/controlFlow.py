# if statement
num = int(input('Please enter a number:'))
if(num > 0):
    print('Positive Number')
elif(num == 0):
    print('Entered Zero')
else:
    print('Negative Number')

# for loop
names = ['Divya', 'Teja', 'Lakshmi']
for name in names:
    print(f"{name} - {len(name)}")

namesObj = {'Divya': 'active', 'Teja': 'inactive', 'Lakshmi': 'active'}
for key in namesObj.items():
    print(f"{key[0]} - {key[1]}")

# range func
# range(start, stop, step)
for i in range(2,10,2):
    print(i)

#break
#continue
#pass
#match
# function annotations - paramter definitions using colon