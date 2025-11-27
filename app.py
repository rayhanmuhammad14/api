from flask import Flask, jsonify

app = Flask(__name__)

datas = {
    'Universitas Muslim Indonesia' : 'Unggul',
    'Universitas Hasanuddin' : 'Unggul'
}

@app.route('/')
def index():
    return jsonify({'datas': datas})

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)