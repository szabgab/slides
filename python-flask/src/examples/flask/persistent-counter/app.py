from flask import Flask
import os
app = Flask(__name__)

def get_counter_file():
    data_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.environ.get('COUNTER_DATA_DIR', data_dir)
    counter_file = os.path.join(data_dir, 'counter.txt')
    return counter_file

@app.route("/")
def main():
    counter_file = get_counter_file()
    counter = 0
    if os.path.exists(counter_file):
        with open(counter_file) as fh:
            counter = int(fh.read())

    counter += 1
    with open(counter_file, 'w') as fh:
        fh.write(str(counter))

    return str(counter)

