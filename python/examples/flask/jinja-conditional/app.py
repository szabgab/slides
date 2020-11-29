from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo.html', text=request.form.get('text', ''))
