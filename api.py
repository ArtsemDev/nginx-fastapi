from fastapi import FastAPI


app = FastAPI()


@app.get(path="/api")
async def index():
    return {"status": "OK"}
