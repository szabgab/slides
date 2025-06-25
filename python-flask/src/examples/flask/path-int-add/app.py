from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Main'

@app.route('/<op>/<int:a>/<int:b>')
def calc(op, a, b):
    if op == 'add':
        return str(a+b)
    if op == 'mul':
        return str(a*b)

    return 'Invalid operator'

@app.route('/sum/<path:values>')
def sum_route(values):
    numbers = map(float, values.split('/'))
    total = sum(numbers)
    return str(total)

