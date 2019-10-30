from flask import Flask, request, render_template, url_for
app = Flask(__name__)
 
@app.route("/")
def main():
    return render_template('main.html')

@app.route("/other")
def other():
    return render_template('other.html',
        img_path = url_for('static', filename='img/python.png'))
