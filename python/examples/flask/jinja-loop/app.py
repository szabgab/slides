from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    languages = [
        'English',
        'Spanish',
        'Hebrew',
        'Hungarian',
    ]
    return render_template('main.html',
        title     = "Code Maven Jinja example",
        languages = languages,
    )
