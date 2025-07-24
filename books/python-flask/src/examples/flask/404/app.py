from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main
<a href="/not">404 page</a>
'''
