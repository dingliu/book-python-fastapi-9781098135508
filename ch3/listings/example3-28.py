# http status code
from fastapi import FastAPI

app = FastAPI()


@app.get("/happy", status_code=200)
def happy():
    return ":)"
