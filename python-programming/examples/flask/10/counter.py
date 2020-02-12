from flask import Flask
app = Flask(__name__)

counter = 1

@app.route("/")
def main():
    global counter
    counter += 1
    return str(counter)

