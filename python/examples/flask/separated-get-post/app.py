from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/calc">calc</a>'

@app.route("/calc", methods=['GET'] )
def calc_get():
    return '''<form method="POST" action="/calc">
        <input name="a">
        <input name="b">
        <input type="submit" value="Compute">
        </form>'''


@app.route("/calc", methods=['POST'] )
def calc_post():
    a = request.form.get('a', '0')
    b = request.form.get('b', '0')
    return str(float(a) + float(b))
