# sido_name의 미세먼지 농도는 dust입니다.
# pm10Value

import requests

# 사용자가 입력한 값으로 요청을 보내보자.
# 사용자가 값을 입력할 수 있는 방법이 필요하다.
sido_Name = input('전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종 중 하나를 입력해 주세요 : ')
key = 'jgo6vyCCraYFb4ZmHP7je6DAFiCZwCd%2FbL73IvqFsgxb2djmFdW0hKqqXf1EOZOEsyUiaxeoNshdAiv73aub0Q%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sido_Name}&ver=1.0'

response = requests.get(url).json()
# print(response_)

"""
목표로 한 수준
"""

# 목표로 한 내용들은 바로 아래 부분

# sido_name = response_['response']['body']['items'][12]['sidoName']
# name = response_['response']['body']['items'][12]['stationName']
# pm = response_['response']['body']['items'][12]['pm10Value']

# print(f'{sido_name}광역시 {name}의 미세먼지 농도는 {pm}입니다.')

"""
응용버전
"""

station_user_input = input('동 명을 입력해 주세요 : ')
items = response['response']['body']['items']

for value in items:
    if value['stationName'] == station_user_input:
        sido_Name = value['sidoName']
        station_name = value['stationName']
        dust = value['pm10Value']

print(f'{sido_Name}시 {station_name}의 미세먼지 농도는 {dust}입니다.')