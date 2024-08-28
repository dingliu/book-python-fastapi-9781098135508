# define a user check dependency
from fastapi import FastAPI, Depends


app = FastAPI()


# dependency func
def check_dep(name: str, password: str):
    if not name:
        raise


@app.get("/check_user", dependencies=Depends(check_dep))
def check_user() -> bool:
    return True
