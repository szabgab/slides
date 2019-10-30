from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def main():
    app.logger.debug("Some debug message")
    app.logger.warning("Some warning message")
    app.logger.error("Some error message")
    return "Hello World"

