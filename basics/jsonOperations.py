import json
obj = {
    "id": 1,
    "name": "user"
}
obj1 = {
  "id": 101,
  "username": "johndoe",
  "name": "John Smith",
  "email": "john.smith@example.com",
  "age": 30,
  "isActive": True,
  "roles": ["User", "Moderator"],
  "address": {
    "street": "123 Maple Street",
    "city": "Pretendville",
    "state": "NY",
    "zipCode": "12345"
  }
}
# dumps and loads method is used to stringify and parse the json data 
serializedVal = json.dumps(obj)
print(serializedVal)

deserizedValue = json.loads(serializedVal)
print(f'Deserialized Value: {deserizedValue}')

# To write json data to a text file, we can use dump, load functions 
f = open('sample.txt', 'w')
json.dump(obj, f) # write json data into file
f.close()

f1 = open('sample.txt', 'r')
data = json.load(f1) # read parsed json from file
print(data)
f1.close()

# writing to json file
j = open('sampleJson.json', 'w')
strVal = json.dumps(obj1)
print(strVal)
j.write(strVal)
j.close()

# we can read the written json back using both read or load
# read will bring the data as string
# load will bring the data as dictionary
j1 = open('sampleJson.json', 'r')
data = j1.read()
print(data)
print(type(data))

j2 = open('sampleJson.json', 'r')
jsonData = json.load(j2)
print(jsonData)
print(type(jsonData))
