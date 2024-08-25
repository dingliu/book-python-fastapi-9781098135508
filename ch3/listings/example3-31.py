# headers
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers.append(name, value)
    return "dummy body"
