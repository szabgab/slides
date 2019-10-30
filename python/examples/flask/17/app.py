from flask import Flask, render_template, url_for, redirect, request, session
app = Flask(__name__)
app.secret_key = 'loginner'

users = {
    'admin' : 'secret',
    'foo'   : 'myfoo',
}

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password and username in users and users[username] == password:
        session['logged_in'] = True
        return redirect(url_for('account'))

    return render_template('login.html')

@app.route("/account")
def account():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('account.html')

@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        return "Not logged in"
    else:
        session['logged_in'] = False
    return render_template('logout.html')


