from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main <a href="/api/info">info</a>
'''

@app.route("/api/info")
def api_info():
    info = {
       "ip" : "127.0.0.1",
       "hostname" : "everest",
       "description" : "Main server",
       "load" : [ 3.21, 7, 14 ]
    }
    return jsonify(info)
