import os
from datetime import timedelta
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User


if os.environ.get("CRYPTID_UNIT_TEST"):
    from fake import user as service
else:
    from service import user as service

from error import MissingError, DuplicateError


ACCESS_TOKEN_EXPIRES_IN_MINUTES = 30

router = APIRouter(prefix="/user")


# --- new auth stuff

# this dependency makes a post to "/user/token"
# (from a form containing a username and a password)
# and returns an access token.
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")


def unauthed():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password.",
        headers={"WWW-Authenticate": "Bearer"},
    )


# This endpoint is directed to by any call that has the
# oauth2_dep() dependency:
@router.post("/token")
async def create_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(oauth2_dep),
):
    """Get username and password from OAuth form, return an access token"""
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN_MINUTES)
    access_token = service.create_access_token({"sub": user.name}, expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    """return the current access token"""
    return {"token": token}
