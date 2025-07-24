from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/user/{user_id}")
async def root(user_id: int, response: Response):
    if user_id > 40:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'detail': 'User does not exist'}
    return {'user': user_id}
