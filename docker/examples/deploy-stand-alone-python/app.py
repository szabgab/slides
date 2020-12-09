from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return 'Calculator'

@app.route("/api/add", methods=['GET'])
def api_add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({
        "a"        :  a,
        "b"        :  b,
        "add"      :  a+b,
    })

#@app.route("/api/multiply", methods=['GET'])
#def api_multiply():
#    a = int(request.args.get('a', 0))
#    b = int(request.args.get('b', 0))
#    return jsonify({
#        "a"        :  a,
#        "b"        :  b,
#        "multiply" :  a*b,
#    })
#
#@app.route("/api/subtract", methods=['GET'])
#def api_subtract():
#    a = int(request.args.get('a', 0))
#    b = int(request.args.get('b', 0))
#    return jsonify({
#        "a"        :  a,
#        "b"        :  b,
#        "subtract" :  a-b,
#    })
#
#
#@app.route("/api/calc")
#def api_calc():
#    a = int(request.args.get('a', 0))
#    b = int(request.args.get('b', 0))
#    div = 'na'
#    if b != 0:
#        div = a/b
#    return jsonify({
#        "a"        :  a,
#        "b"        :  b,
#        "add"      :  a+b,
#        "multiply" :  a*b,
#        "subtract" :  a-b,
#        "divide"   :  div,
#    })

