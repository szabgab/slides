from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"

@app.route("/login")
def login():
    return "Showing the login page ..."
