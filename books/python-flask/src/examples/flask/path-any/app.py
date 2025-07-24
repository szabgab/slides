from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '''
Main<br>
<a href="/user/name">/user/name</a><br>
<a href="/user/other/dir">/user/other/dir</a><br>
<a href="/user/hi.html">/usre/hi.html</a><br>
'''

@app.route("/user/<path:fullpath>")
def api_info(fullpath):
    return fullpath
