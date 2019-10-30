from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main <a href="/add/23/19">add</a>
'''

@app.route("/add/<int:a>/<int:b>")
def api_info(a, b):
    return str(a+b)


