from flask import Flask, request, render_template
app = Flask(__name__)

counter = 1
 
@app.route("/")
def hello():
    global counter
    counter += 1
    return str(counter)
 
