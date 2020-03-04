from flask import Flask
from flask_redis import Redis
app = Flask(__name__)
redis = Redis(app)

@app.route('/')
def hello():
    return "Hello World- Trambo!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')