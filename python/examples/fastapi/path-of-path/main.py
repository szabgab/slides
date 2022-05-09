from fastapi import FastAPI

app = FastAPI()

@app.get("/file/{filepath}")
async def get_filename(filepath: str):
    return {f"path: '{filepath}'"}

@app.get("/deep/{filepath:path}")
async def get_path(filepath: str):
    return {f"path: '{filepath}'"}
