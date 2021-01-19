from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import json

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


@app.route('/themes', methods=['POST'])
def save_new_theme():
    name = request.form['name']
    emoji = request.form['emoji']
    spot1 = request.form['spot1']
    spot1_lat = request.form['spot1_lat']
    spot1_lng = request.form['spot1_lng']
    spot2 = request.form['spot2']
    spot2_lat = request.form['spot2_lat']
    spot2_lng = request.form['spot2_lng']
    spot3 = request.form['spot3']
    spot3_lat = request.form['spot3_lat']
    spot3_lng = request.form['spot3_lng']

    newthemes = {'name': name, 'emoji': emoji, 'spot1': spot1, 'spot1_lat': spot1_lat, 'spot1_lng': spot1_lng, 'spot2': spot2, 'spot2_lat': spot2_lat, 'spot2_lng': spot2_lng, 'spot3': spot3, 'spot3_lat': spot3_lat, 'spot3_lng': spot3_lng}
    db.new_theme.insert_one(newthemes)
    return jsonify({'result': 'success'})


# 테마 모두 조회하는 API
@app.route('/themes', methods=['GET'])
def read_themes():
    themes = list(db.new_theme.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'new_theme': themes})


# 테마 하나만 조회하는 API
@app.route('/detail', methods=['GET'])
def read_detail():
    name = request.args.get('name')
    detail = db.new_theme.find_one({'name': name}, {'_id': 0})

    return jsonify({'result': 'success', 'detail': detail})

@app.route('/emoji')
def get_data():
  return app.send_static_file('full-emoji-list.json')

with open('C:\\Users\\LG\\Desktop\\sparta\\my_project\\travel\\static\\full-emoji-list.json',encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
