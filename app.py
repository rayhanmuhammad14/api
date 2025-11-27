from flask import Flask, jsonify, request

app = Flask(__name__)

def tambah(angka1, angka2):
    return angka1+angka2

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        datas = request.get_json()
        datas1 = datas['a']
        datas2 = datas['b']
        
        hasil = tambah(datas1, datas2)
    
        return jsonify({'datas': hasil})
    
    return jsonify({'pesan':'Anda Belum Memasukkan Data apapun'})

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)