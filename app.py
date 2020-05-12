import os
import mimetypes
from flask import Flask, abort, Response, redirect

app = Flask(__name__)

root = os.path.dirname(os.path.abspath(__file__))
#html = os.path.join(root, 'html')

def show(filename):
    path = os.path.join(root, "html", filename)
    if os.path.isdir(path):
        if filename[-1] != "/":
            return redirect(filename + "/")
        path = os.path.join(path, "index.html")

    if not os.path.exists(path):
        app.logger.warning(f"file '{filename}' does not exist")
        abort(404)

    _, ext = os.path.splitext(filename)
    #if ext and ext != '.html':
    mimetype = mimetypes.types_map.get(ext)
    app.logger.info(f"mimetype of '{filename}' is '{mimetype}'")
        #add_header(f"Content-type: {mimetype}")

    with open(path, 'rb') as fh:
        content = fh.read()
    return Response(content, mimetype=mimetype)

@app.route("/")
def main_main():
    return show("index.html")


@app.route("/<path:relpath>")
def any_page(relpath):
    #if relpath in ["favicon.ico"]:
    #    abort(404)
    return show(relpath)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
