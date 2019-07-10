from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo.html', text=request.form['text'])
