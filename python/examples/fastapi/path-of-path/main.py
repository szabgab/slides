from fastapi import FastAPI

app = FastAPI()

@app.get("/shallow/{filepath}")
async def get_filename(filepath: str):
    return {'shallow': filepath}

@app.get("/deep/{filepath:path}")
async def get_path(filepath: str):
    return {'deep': filepath}
