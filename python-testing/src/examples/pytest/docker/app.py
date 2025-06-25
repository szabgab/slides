from flask import Flask, jsonify, request
import time
calcapp = Flask(__name__)

@calcapp.route("/")
def main():
    return 'Post JSON to /api/calc'

@calcapp.route("/api/calc")
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({
        "a"        :  a,
        "b"        :  b,
        "add"      :  a+b,
    })

