# return a user dependency
# As of FastAPI v0.112.2 there is no 'Params' under fastapi module.
#
# When defined as below, the `user_dep` dependency function discovers
# `name` and `password` query parameters automatically.
from fastapi import FastAPI, Depends

app = FastAPI()


# the dependency func
def user_dep(name: str, password=str):
    return {"name": name, "valid": True}


# the path function / web endpoint
@app.get("/user")
def get_user(user: dict = Depends(user_dep)):
    return user
