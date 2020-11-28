from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/goto">Go to</a>'

@app.route('/goto')
def goto():
    return redirect(url_for('user_page'))

@app.route('/user')
def user_page():
    return 'User page'
