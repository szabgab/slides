from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("nhoj"),
    "jane": generate_password_hash("enaj")
}

@app.route("/")
def hello():
    return "Hello World!"

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route("/admin")
@auth.login_required
def admin():
    return "Hello Admin"

