from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/login">login</a>'

@app.route('/login')
def login_get():
    return '''<form action="/login" method="POST">
            <input name="username">
            <input name="password" type="password">
            <input type="submit" value="Login">
        </form>'''

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if password is None or username is None:
        return redirect(url_for('login_get'))
    if password == username: # do the real verification here
        return redirect(url_for('user_page', name = username))
    return redirect(url_for('login_get'))

@app.route('/user/')
def user_page_central():
    return 'List of users'

@app.route('/user/<name>')
def user_page(name):
    return f'Page of {name}'
