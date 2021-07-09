import requests

name = input('name: ')
age = int(input('age: '))

data = requests.get(url=f'http://127.0.0.1:5000/{name}/{age}')

print(data.json())