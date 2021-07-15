import requests

name = 'viktor'

url = f'https://api.agify.io/?name={name}'

# 이건 str 타입
response = requests.get(url).text
print(response)
# 이건 dict 타입
response = requests.get(url).json()
print(response)

# name의 나이는 age입니다.

name = response['name']
age = response['age']

print(f'{name}의 나이는 {age}살 입니다.')