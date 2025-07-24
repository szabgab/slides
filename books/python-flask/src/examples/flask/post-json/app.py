from flask import Flask, jsonify, render_template, request
import time
app = Flask(__name__)

@app.route("/")
def main():
    return 'Post JSON to /api/calc'

@app.route("/api/calc", methods=['POST'])
def add():
    data = request.get_json()
    if data is None:
        return jsonify({ 'error': 'Missing input' }), 400
    a = int(data.get('a', 0))
    b = int(data.get('b', 0))
    div = 'na'
    if b != 0:
        div = a/b
    return jsonify({
        "a"        :  a,
        "b"        :  b,
        "add"      :  a+b,
        "multiply" :  a*b,
        "subtract" :  a-b,
        "divide"   :  div,
    })

