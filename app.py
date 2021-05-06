from flask import Flask, render_template,url_for,request,jsonify
from pororo import Pororo
import random
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/study",methods=['POST'])
def study():
    # t = 公司安排我下午出差。
    # a = '회사는 내가 오후에 출장 가는 것으로  처리했다.'
    if request.method=='POST':
        lableSen = request.form['kosen']
        sen = request.form['zhsen']
        targetSen = sen.strip()
        print(targetSen)
        tk = Pororo(task='tokenize',lang='zh')
        tokens = tk(targetSen)
        print(tokens)
        random.shuffle(tokens)
        jsonify(tokens)
    return render_template('studymode.html',value=tokens,translation=lableSen)


if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)