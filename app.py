from flask import Flask, request
import requests

app = Flask(__name__)

def token_required(f):
    def decorated(*args, **kwargs):
        authorization = request.headers["Authorization"]
        if not authorization:
            return {'error': 'token is missing'}, 403
        
        if "Bearer" in authorization:
            try:
                [token_type, token] = authorization.split(" ")
            except Exception as error:
                return {'error': 'token is invalid/expired'}, 401
       
        if token:
            try:
                # jwt.decode(token, app.config['secret_key'], algorithms="HS256")
                # jwt.decode(token, '', algorithms="HS256")
                payload = 'client_id=aaa&client_secret=bbb&token='+token
                r = requests.post('https://httpbin.org/post', data=payload)
                print(r)
            except Exception as error:
                return {'error': 'token is invalid/expired'}, 401
            return f(*args, **kwargs)
    return decorated



response = [
    {"price": 16.99}
]

@app.get("/")
@token_required
def list_item():
    return response