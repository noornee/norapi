from flask import Flask, jsonify
from flask import send_from_directory
import os
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')



@app.route('/', methods=['GET'])
@app.route('/home')
def anime_data():
    with open('anime_data.json') as doc:
        data = json.load(doc)
        json_data = jsonify(data)
        return json_data


@app.route('/<int:id>', methods=['GET'])
@app.route('/home/<int:id>')
def get_data_by_id(id):
    with open('anime_data.json') as doc:
        data = json.load(doc)
        temp = data['anime_list']
        for i in temp:
            if i['id'] == id:
                json_data = jsonify(i)
                return json_data


@app.route('/<slug>', methods=['GET'])
@app.route('/home/<slug>')
def get_data_by_slug(slug):
    with open('anime_data.json') as doc:
        data = json.load(doc)
        temp = data['anime_list']
        for i in temp:
            if i['slug'] == slug:
                json_data = jsonify(i)
                return json_data


if __name__ == '__main__':
    app.run(debug=True)
