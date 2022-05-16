from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_id}")
async def root(user_id: int):
    return {'user': user_id}
