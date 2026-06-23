# using requests and httpx libraries, we can access external apis
# requests is synchronous and it has no timeout
# httpx is asynchronous and it has 5secs timeout
import requests
import httpx
import asyncio
import json

# requests
# post
payload = {'userId': 11, 'id': 201, 'title': 'Testing'}
postResponse = requests.post('https://jsonplaceholder.typicode.com/todos', json=payload)
print(postResponse.json())

# delete
response = requests.delete('https://jsonplaceholder.typicode.com/todos/1')
print(response.json())

# get all
response = requests.get('https://jsonplaceholder.typicode.com/todos')
data = response.json()
print({
    'TotalCount': len(data),
})

# put
response = requests.put('https://jsonplaceholder.typicode.com/todos/1', json={'title': 'afdjask afdajksd'})
print(response.json())

# get
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.json())

# httpx
response1 = httpx.get('https://jsonplaceholder.typicode.com/users')
f = open('sampleJson.json', 'w')
json.dump(response1.json(), f)
# print(response1.json())
f.close()

# asynchronous api calls
async def fetchUsers():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/users')
        await asyncio.sleep(2)
        print({
            'users': len(response.json())
        })
        return response.json()

async def fetchPost():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/posts/1')
        print({
            'posts': len(response.json())
        })
        return response.json()

result = asyncio.run(fetchUsers())
result1 = asyncio.run(fetchPost())

# run apis parallely
async def main():
    await asyncio.gather(
        fetchUsers(),
        fetchPost()
    )
asyncio.run(main())