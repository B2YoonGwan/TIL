import requests
from bs4 import BeautifulSoup

# 요청할 url 선언
url = 'https://finance.naver.com/marketindex/'
# 응답 받은 문서를 문자열로 반환
response = requests.get(url).text
# bs4를 통해 파이썬이 읽을 수 있는 데이터 형으로 변경
# 변경하는 문서가 어떤 형태인지도 같이 작성해 줘야 한다.
# html.parser -> html 문서를 파이썬에서 읽을 수 있도록 만들어준다.
data = BeautifulSoup(response, 'html.parser')

# 원하는 정보가 담겨있는 것을 가져오는 것
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# print(type(response))
# print(type(data))

# print(kospi)
# print(type(kospi))

result = exchange.text

# 현재의 원/달러 환율은 result입니다.
print(f'현재의 원/달러의 환율은 {result}입니다.')