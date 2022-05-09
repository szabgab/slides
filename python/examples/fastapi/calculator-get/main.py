from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(a: int, b: int):
    return {"message": a+b}
