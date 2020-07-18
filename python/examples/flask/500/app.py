from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main
<a href="/bad">bad</a>
'''

@app.route("/bad")
def bad():
    raise Exception("This is a bad page")
    return 'Bad page'
