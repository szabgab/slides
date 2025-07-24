from fastapi import FastAPI
import os
root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(root, 'counter.txt')

app = FastAPI()

@app.get("/")
async def main():
    if os.path.exists(filename):
        with open(filename) as fh:
            counter = int(fh.read())
    else:
        counter = 0
    counter += 1
    with open(filename, 'w') as fh:
        fh.write(str(counter))

    return {"cnt": counter}

