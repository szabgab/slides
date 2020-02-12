from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']
