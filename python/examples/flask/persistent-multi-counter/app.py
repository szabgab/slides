from flask import Flask
import os
import json
app = Flask(__name__)

def get_counter_file():
    data_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.environ.get('COUNTER_DATA_DIR', data_dir)
    counter_file = os.path.join(data_dir, 'counter.json')
    return counter_file

def read_counters():
    counter_file = get_counter_file()
    counter = {}
    if os.path.exists(counter_file):
        with open(counter_file) as fh:
            counter = json.load(fh)
    return counter

@app.route("/")
def main():
    counter = read_counters()
    if not counter:
        return 'No counter yet. Maybe start by clicking <a href="/python">here</a>'

    html = '<table>\n'
    for name in sorted(counter.keys()):
        html += f'<tr><td><a href="/{name}">{name}</a></td><td>{counter[name]}</td></tr>\n'
    html += '</table>'
    return html

@app.route("/<name>")
def count(name):
    counter = read_counters()

    if name not in counter:
        counter[name] = 0
    counter[name] += 1

    counter_file = get_counter_file()
    with open(counter_file, 'w') as fh:
        json.dump(counter, fh)

    return f'<a href="/">home</a> {name}: {counter[name]}'


