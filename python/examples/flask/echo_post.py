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
    return "You said: " + request.form['text']
 
 
if __name__ == "__main__":
    app.run()
