from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    languages = [
        {
            "name": "Python",
            "year":  1991,
        },
        {
            "name": "JavaScript",
            "year":  1995,
        },
        {
            "name": "C",
        }
    ]
    return render_template('main.html',
        title     = "Code Maven Jinja example",
        languages = languages,
    )
