from flask import Flask, request, jsonify, make_response
import jwt, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sesdadqweas12312@@@#1234'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username','')
    password = data.get('password','')
    if username == 'admin' and password == 'senha123':
        token = jwt.encode({'sub': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'], algorithm='HS256')
        resp = make_response(jsonify({"msg":"logado"}), 200)
        resp.set_cookie('session', token, httponly=True, samesite='Strict', secure=False)  # em prod: secure=True
        return resp
    return jsonify({"msg":"credenciais inválidas"}), 401

if __name__ == '__main__':
    app.run(port=5000)
