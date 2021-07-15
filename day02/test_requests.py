# 파이썬으로 요청 보내기 위한 준비
# requests 라는 모듈을 사용 할거다.
import requests

# requests로 https://www.naver.com 으로 요청 보낸 결과 출력
print(requests.get('https://www.naver.com'))
# requests.get('주소').text() 하면 텍스트를 보여줌 -> 엄청난 텍스트
print(requests.get('https://www.naver.com').text)
# requests.get('주소').status_code 하면 상태만 보여줌 -> 200
print(requests.get('https://www.naver.com').status_code)


























