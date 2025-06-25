from fastapi import FastAPI, Response
import os
root = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

@app.get("/")
async def main():
    #print(root)
    with open(os.path.join(root, 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

