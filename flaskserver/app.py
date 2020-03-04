from flask import Flask
import redis
import os
USER = os.getenv('ENV_USER')
r = redis.Redis(host='localhost', port=6379, db=0)
#from flask_redis import Redis
app = Flask(__name__)
#redis = Redis(app)

@app.route('/')
def hello():
    return "Hello World- Trambo!-> ENV   "+USER

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')