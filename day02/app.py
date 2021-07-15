from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# 127.0.0.1:5000/ssafy로 주소를 입력했을 때
@app.route('/ssafy')
# hello ssafy라는 내용을 반환하는 함수 ssafy를 작성하고
def ssafy():
    return "hello ssafy!"
# 브라우저에서 직접 들어가서 결과물 확인해보자.

if __name__ == '__main__':
    app.run(debug=True)