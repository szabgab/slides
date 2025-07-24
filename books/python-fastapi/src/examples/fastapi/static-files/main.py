import os

from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

root = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

app.mount("/js", StaticFiles(directory=os.path.join(root, 'js')), name="js")

@app.get("/")
async def main():
    with open(os.path.join(root, 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")


