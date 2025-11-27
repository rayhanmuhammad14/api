from flask import Flask, jsonify

api = Flask(__name__)

datas = {
    'Universitas Muslim Indonesia' : 'Unggul',
    'Universitas Hasanuddin' : 'Unggul'
}

@api.route('/')
def index():
    return jsonify({'datas': datas})

if __name__ == '__main__':
    api.run('0.0.0.0', debug=True)