import os

from fastapi import FastAPI, Response
from api_v1 import api_v1

root = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

app.mount("/api/v1", api_v1)

@app.get("/")
async def main():
    return Response(content='main <a href="/api/v1">/api/v1</a>', media_type="text/html")

