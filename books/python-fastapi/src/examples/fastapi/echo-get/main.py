from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(text):
    return {"message": f"You wrote: '{text}'"}

