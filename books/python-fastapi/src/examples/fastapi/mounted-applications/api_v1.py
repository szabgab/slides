from fastapi import FastAPI

api_v1 = FastAPI()


@api_v1.get("/")
def main():
    return {"message": "Hello World from API v1"}



