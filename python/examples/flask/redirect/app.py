from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/cm">Go to Code Maven</a>'

@app.route('/cm')
def cm():
    return redirect('https://code-maven.com/')
