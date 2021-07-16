# Flask 불러온다.
# Flask는 파이썬이 기본으로 가지고 있는 모듈이 아니다.
# 그럼 설치한다. pip를 통해.
# pip install Flask -> bash창에 입력해서 설치한다.

from flask import Flask, render_template, request
import requests

# 함수안에서 일일이 선언하지 않기 위해 제일 위에 global로 TOKEN과 url 선언
TOKEN = '1839869313:AAHW4NuS-EW_NMiV6FV10twmAAYPXmGLfvE'
url = f'https://api.telegram.org/bot{TOKEN}'

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# Flask로 어떤 문서를 응답할때, return에 작성하는 것이 아니라, 특정 문서 자체를 불러와서 응답해줄 수 있다.
# render_template
# flask가 가지고 있는 함수 render_template을 불러와야 한다.
# html문서 하나 만들건데 그 문서를 보여주는 페이지 만들기

@app.route('/ssafy')
def ssafy():
    # ssafy.html을 rendering 한다.
    return render_template('ssafy.html')

# 로그인이든 아니면 채팅이든
# 내가 입력한 값을 보낼 수 있는
# 메시지를 보낼 수 있고
# 보내온 메시지를 받아서 어떤 행위를 실행하는 코드
# 함수가 2개 필요하다.

# write함수(메시지를 입력하는 곳), send함수(메시지를 받는 곳)
@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # 사용자가 요청보낸 정보 확인할 수 있는 request를 불러온다.
    # print(request)
    # print(dir(request))
    # write.html로 작성한 내용을 request를 통해서 가져와서 담는 코드
    message = request.args.get("message")
    
    # 텔레그램 챗봇 api url 필요
    # 내 챗봇 토큰 필요
    # 봇 토큰 변수에 담기
    TOKEN = '1839869313:AAHW4NuS-EW_NMiV6FV10twmAAYPXmGLfvE'
    # 요청 통합 URL 변수에 담기
    url = f'https://api.telegram.org/bot{TOKEN}'
    # 메세지 보낼 사람 chat_id 필요
    # 토큰에 있는 아이디가 아니라 getUpdates로 들어갔을 때 나오는 id를 입력해야한다.
    chat_id = 1848368530
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'
    # 파이썬으로 요청보내는 requests 필요
    requests.get(send_message_url)
    return render_template('send.html')


# 주소 함수이름이랑 동일하게 작성한다.
# html 이름도 함수 이름이랑 동일하게 작성한다.
# 안의 내용은 일단 제목만 입력해서
# 두 페이지 정상작동하는지 확인

# POST 방식의 요청만 받겠다.
@app.route('/telegram', methods=['POST'])
def telegram():
        # 요청 정보는 request에 들어있따.
    response = request.get_json()
    print(response)
    """
    response에 담긴 내용
    {
        'update_id': 791494220, 
        'message': {
            'message_id': 8, 
            'from': {
                'id': 1848368530, 
                'is_bot': False, 
                'first_name': 'Yoon', 
                'last_name': 'Gwan', 
                'language_code': 'ko'
                }, 
            'chat': {
                'id': 1848368530, 
                'first_name': 'Yoon', 
                'last_name': 'Gwan', 
                'type': 'private'
                }, 
            'date': 1626413417, 
            'text': '하이'
        }
    }
    """
    # response에 chat_id, text 들어있다.
    # text에 들어있는 값이 무엇인지에 따라서 보낼 메시지를 바꿔주면 된다.
    # 조건문을 넣어주면 될 것 같다.
    # 1. 사용자가 챗봇한테 보낸 메시지 똑같이 돌려보내주는 코드 작성
    # 2. '누구야'라고 왔을 때, 저는 ~~님의 챗봇입니다 라고 돌려보내주는 코드 작성
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == '누구야?':
        text = '저는 윤관님의 챗봇입니다.'
    # 3. 어제 작성한 미세먼지 API 코드 가져와서 '미세먼지'라고 입력 받으면
    # 미세먼지 정보를 알려주는 코드 작성
    # 민지님 key 확인하시고 검색하고 싶은 도시 확인해서 
    # sido_Name, sido_name, station_name, dust에 넣으시면 됩니다.
    elif text == '미세먼지':
        key = 'jgo6vyCCraYFb4ZmHP7je6DAFiCZwCd%2FbL73IvqFsgxb2djmFdW0hKqqXf1EOZOEsyUiaxeoNshdAiv73aub0Q%3D%3D'
        sido_Name = '대구'
        # 이 dust_url은 미세먼지 api의 url이므로 변수명을 다르게 선언해줬습니다.
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sido_Name}&ver=1.0'
        response = requests.get(dust_url).json()
        sido_name = response['response']['body']['items'][12]['sidoName']
        station_name = response['response']['body']['items'][12]['stationName']
        dust = response['response']['body']['items'][12]['pm10Value']
        text = f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다.'
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url).json()

    # 이까지 완성하시고 교재에 나온 pythonanywhere 여기에 올리시면 됩니다!


    
    # 응답은 본문과 status_code 200을 같이 보내준다.

    return '', 200


# 이 debug관련 코드는 무조건 파일의 마지막에 위치해야 한다.
# 중간에 들어가면 뒤에 코드들이 실행되지 않음.
if __name__ == '__main__':
    app.run(debug=True)