import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()


secret_user: str = "newphone"
secret_password: str = "whodis?"


basic = HTTPBasic()


@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if creds.username == secret_user and creds.password == secret_password:
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Hey!")


if __name__ == "__main__":
    uvicorn.run("auth:app", reload=True)
