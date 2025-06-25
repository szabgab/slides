from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def main(response: Response):
    response.headers['X-something-else'] = "some value"
    return {"message": "Hello World"}

