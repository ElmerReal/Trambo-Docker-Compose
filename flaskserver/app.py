from flask import Flask
import redis
import os
ENV_HOST = os.getenv('ENV_HOST')
ENV_PORT = os.getenv('ENV_PORT')
ENV_DB = os.getenv('ENV_DB')
r = redis.Redis(host=ENV_HOST, port=ENV_PORT, db=ENV_DB)
r.mset({"Jhon": "22 years", "Jhon": "30 years"})
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World- Trambo!-> ENV   "+ENV_HOST

@app.route('/1')
def hello1():
    return r.get("Jhon")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')