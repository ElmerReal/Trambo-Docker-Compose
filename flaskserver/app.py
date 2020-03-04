from flask import Flask
import redis
import os
ENV_HOST = os.getenv('ENV_HOST')
ENV_PORT = os.getenv('ENV_PORT')
ENV_DB = os.getenv('ENV_DB')
r = redis.Redis(host=ENV_HOST, port=ENV_PORT, db=ENV_DB)
r.mset({"Jhon": "22 years", "Jhon": "30 years"})
app = Flask(__name__)

@app.route('/Guardar/<username>/<age>')
def hello(username,age):
    r.set(username,age)
    return " [ "+username+" ] Guardado correctamente"

@app.route('/Listar')
def hello1():
    return str(r.keys("*"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')