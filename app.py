from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # 인스타그램 주소로 리다이렉트
    return redirect("https://www.instagram.com/leeewooks/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
