from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def root():
    data = '<a href="/hello">hello</a>'
    return Response(content=data, media_type="text/html")


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}

