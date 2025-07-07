from flask import Flask, request, jsonify
import os
import datetime

version = 1

app = Flask(__name__)

filename = 'counter.txt'
dirname = os.environ.get('COUNTER_DIR')
if dirname:
    filename = os.path.join(dirname, filename)

@app.route("/", methods=['GET'])
def main():
    now = datetime.datetime.now()

    counter = 0
    if os.path.exists(filename):
        with open(filename) as fh:
            counter = int(fh.read())
    counter += 1
    with open(filename, 'w') as fh:
        fh.write(str(counter))

    return f'''
        <html>
          <head><title>Calculator v{version}</title></head>
          <body>App v{version} at {now} count: {counter}</body>
        </html>
    '''


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

