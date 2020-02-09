from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
     <form action="/echo" method="POST">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''

@app.route("/echo", methods=['POST'])
def echo():
    if 'text' in request.form:
        return "You said: " + request.form['text']
    else:
        return "Nothing to say?"

