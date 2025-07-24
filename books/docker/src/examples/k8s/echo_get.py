from flask import Flask, request
app = Flask(__name__)

VERSION = "1.00"

@app.route("/")
def main():
    return f'''
     VERSION {VERSION}<br>
     <form action="/echo" method="GET">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''

@app.route("/echo")
def echo():
    return "You said: " + request.args.get('text', '')
