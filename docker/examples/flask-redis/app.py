from flask import Flask, request, render_template
import redis
app = Flask(__name__)

r = redis.Redis(host='my-redis', port=6379, db=0)

@app.route("/")
def main():
    return render_template('red.html')

@app.route("/save", methods=['POST'])
def save():
    field = request.form['field']
    value = request.form['value']
    ret = r.set(field, value)
    app.logger.debug(ret)
    new_value = r.get(field)
    return render_template('red.html', saved=1, value=new_value)

@app.route("/get", methods=['POST'])
def get():
    field = request.form['field']
    value = r.get(field)
    if value is None:
        return render_template('red.html', field=field, value="Not defined yet")
    str_value = value.decode('utf-8')
    return render_template('red.html', field=field, value=str_value)
