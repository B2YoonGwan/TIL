# setWebhook 요청 보내야 한다.
# ngrok이라는 임시 서버를 활용하기 위한 코드
import requests

# token, url, ngrok url
# 봇 토큰 변수에 담기
TOKEN = '1839869313:AAHW4NuS-EW_NMiV6FV10twmAAYPXmGLfvE'
# 요청 통합 URL 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
# ngrok http 5000 -> https://url 복사 -> 우클릭
ngrok_url = 'https://be06e3dd6e41.ngrok.io'

# python_anywhere에 올렸으므로 경로 변경
# 처음에 주소 받아오면 http인데 webhook은 https만 받을 수 있으므로 s추가
python_anywhere = 'https://yoongwan.pythonanywhere.com'
set_webhook_url = f'{url}/setWebhook?url={python_anywhere}/telegram'
# telegram이 내 ngrok/telegram으로 요청을 보내고, 200 응답받아간다.

response = requests.get(set_webhook_url)
print(response.text)

