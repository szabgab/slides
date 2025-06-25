from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    person = {
        'fname' : 'Mary',
        'lname' : 'Ann',
        'email' : 'mary-ann@example.com',
    } 
    return render_template('main.html',
        title     = 'Person',
        person    = person,
    )
