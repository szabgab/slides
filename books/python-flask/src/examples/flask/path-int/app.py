from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main<br>
<a href="/user/23">23</a><br>
<a href="/user/42">42</a><br>
<a href="/user/Joe">Joe</a><br>
'''

@app.route("/user/<int:uid>")
def api_info(uid):
    return str(uid)
