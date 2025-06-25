from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_name}")
async def root(user_name: str):
    return {'msg': f"user '{user_name}'"}
