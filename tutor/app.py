from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.travel


## HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new_theme')
def new_theme():
    return render_template('new_theme.html')


@app.route('/theme', methods=['POST'])
def save_new_theme():
    name = request.form['name']
    emoji = request.form['emoji']
    spot1 = request.form['spot1']
    spot2 = request.form['spot2']
    spot3 = request.form['spot3']


    newtheme = {'name': name, 'emoji': emoji, 'spot1': spot1, 'spot2': spot2, 'spot3': spot3}
    db.new_theme.insert_one(newtheme)

    return jsonify({'result': 'success'})

# 테마 모두 조회하는 API
@app.route('/theme', methods=['GET'])
def read_themes():
    themes = list(db.new_theme.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'new_theme': themes})

# 테마 하나만 조회하는 API
@app.route('/detail', methods=['GET'])
def read_detail():
    name = request.args.get('name')
    detail = db.new_theme.find_one({name: name}, {'_id': 0})
    return jsonify({'result': 'success', 'detail': detail})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)