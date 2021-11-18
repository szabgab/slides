from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo" method="GET">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''

@app.route("/echo")
def echo():
    user_text = request.args.get('text', '')
    if user_text:
        return "You said: " + user_text
    return "Nothing to say?"
