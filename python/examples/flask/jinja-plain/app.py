from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/echo", methods=['POST'])
def echo():
    user_text = request.form.get('text', '')
    return "You said: " + user_text
