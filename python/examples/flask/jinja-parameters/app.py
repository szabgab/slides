from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo():
    user_input = request.form.get('text', '')
    return render_template('echo.html', text=user_input)
