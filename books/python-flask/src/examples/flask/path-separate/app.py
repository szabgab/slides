from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return '''
Main<br>
<a href="/user/23">23</a><br>
<a href="/user/42">42</a><br>
<a href="/user/Joe">Joe</a><br>
'''

@app.route("/user/<uid>")
def api_info(uid):
    return uid

@app.route("/user/")
def user():
    return 'User List'
