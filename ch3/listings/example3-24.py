# post data in header
from fastapi import FastAPI, Header

app = FastAPI()


@app.post("/hi")
def greet(who: str = Header()):
    return f"Hello {who}!"
