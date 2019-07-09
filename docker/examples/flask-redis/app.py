from flask import Flask, request, render_template
import redis
app = Flask(__name__)

r = redis.Redis(host='flask-redis_redis_1', port=6379, db=0)

@app.route("/")
def hello():
    return render_template('red.html')

@app.route("/save", methods=['POST'])
def save():
    field = request.form['field']
    value = request.form['value']
    r.set(field, value)
    new_value = r.get(field)
    return render_template('red.html', saved=1, value=new_value)

@app.route("/get", methods=['POST'])
def get():
    field = request.form['field']
    value = r.get(field)
    return render_template('red.html', field=field, value=value)
