from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def main(request: Request):
    print(request.headers)
    # Headers({
    #     'host': 'testserver',
    #     'user-agent': 'testclient',
    #     'accept-encoding': 'gzip, deflate',
    #     'accept': '*/*',
    #     'connection': 'keep-alive',
    #     'x-some-field': 'a value'
    # })

    #print(request.client)
    print(request.client.host) # testclient
    print(request.client.port) # 50000
    return {"message": "Hello World"}

