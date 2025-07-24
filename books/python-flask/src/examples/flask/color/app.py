from flask import Flask, request, render_template, session
import re
app = Flask(__name__)
app.secret_key = 'blabla'

@app.route("/",methods=['GET', 'POST'] )
def main():
    color = session.get('color', 'FFFFFF')
    app.logger.debug("Color: " + color)

    new_color = request.form.get('color', '')
    if re.search(r'^[0-9A-F]{6}$', new_color):
        app.logger.debug('New color: ' + new_color)
        session['color'] = new_color
        color = new_color

    return render_template('main.html', color = color)

