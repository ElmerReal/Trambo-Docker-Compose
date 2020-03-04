from flask import Flask
import redis
import os
ENV_HOST = os.getenv('ENV_HOST')
ENV_PORT = os.getenv('ENV_PORT')
ENV_DB = os.getenv('ENV_DB')


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World- Trambo!-> ENV   "+USER

@app.route('/1')
def hello1():
    r = redis.Redis(host=ENV_HOST, port=ENV_PORT, db=ENV_DB)
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    return r.get("Bahamas")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')