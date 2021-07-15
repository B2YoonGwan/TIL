# requests를 불러온다.
# 요청 보낼 url을 작성한다.
# 이름과 함께 요청을 보낸다.
# 응답받은 값을 json 함수를 통해 dict로  변환한다.
# 응답받은 결과의 형태를 확인하고
# 첫 번째 결과물에서 국가명과 확률을 뽑는다.
# 확률은 소수로 변경해서 퍼센테이지 형태로 변환한다.
# 곱셉은 *을 사용.

import requests
name = 'viktor'
url = f'https://api.nationalize.io/?name={name}'

# dict 타입
response = requests.get(url).json()
print(response)

country_id = response['country'][0]['country_id']
prob = response['country'][0]['probability'] * 100
name = response['name']

# round 내장함수로 반올림 가능
# round()
print(f'{name}의 국가는 {round(prob, 3)}% 확률로 {country_id}입니다.')




