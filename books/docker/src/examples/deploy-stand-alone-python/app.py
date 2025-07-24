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
          <head><title>Demo v{version}</title></head>
          <body>Demo v{version} at {now} count: {counter}</body>
        </html>
    '''

