from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'] )
def main():
    color = "FFFFFF"
    new_color = request.form.get('color', '')
    if re.search(r'^[0-9A-F]{6}$', new_color):
        color = new_color

    return render_template('main.html', color = color)
