from fastapi import FastAPI, Response
import json
import os
root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(root, 'counter.json')

app = FastAPI()

@app.get("/{name}")
async def count(name):
    counters = load_counters()
    if name not in counters:
        counters[name] = 0

    counters[name] += 1

    with open(filename, 'w') as fh:
        json.dump(counters, fh)

    return {"cnt": counters[name]}

@app.get("/")
async def main():
    counters = load_counters()
    if counters:
        html = '<table>\n'
        for name in sorted(counters.keys()):
            html += f'<tr><td><a href="/{name}">{name}</a></td><td>{counters[name]}</td></tr>\n'
        html += '</table>\n'
    else:
        html = 'Try accessing <a href="/foo">/foo</a>';
    return Response(content=html, media_type="text/html")


def load_counters():
    if os.path.exists(filename):
        with open(filename) as fh:
            counters = json.load(fh)
    else:
        counters = {}

    return counters

