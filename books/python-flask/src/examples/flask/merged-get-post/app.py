from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/calc">calc</a>'

@app.route("/calc", methods=['GET', 'POST'] )
def calc():
    if request.method == 'POST':
        a = request.form.get('a', '0')
        b = request.form.get('b', '0')
        return str(float(a) + float(b))
    else:
        return '''<form method="POST" action="/calc">
            <input name="a">
            <input name="b">
            <input type="submit" value="Compute">
            </form>'''

