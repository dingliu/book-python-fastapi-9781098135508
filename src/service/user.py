import os
from datetime import timedelta, datetime
from jose import jwt, JWTError
from model.user import User

if os.environ.get("CRYPTID_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data

# --- New auth stuff

from passlib.context import CryptContext

# CHANGE SECRET_KEY FOR PRODUCTION!
SECRET_KEY = os.environ.get("SECRET_KEY", "keep-it-secret-keep-it-safe")
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    """Hash <plain> and compare with <hash> from the database."""
    return pwd_context.verify(plain, hash)


def get_hash(plain: str) -> str:
    """return the hash of a <plain> str."""
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    """return username from JWT access <token>."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except JWTError:
        return None
    return username


def get_current_user(token: str) -> User | None:
    """decode an OAuth access <token> and return the User."""
    if not (username := get_jwt_username(token)):
        return None
    if user := lookup_user(username):
        return user
    return None


def lookup_user(username: str) -> User | None:
    """return a matching User from the database for <username>."""
    if user := data.get_one(username):
        return user
    return None


def auth_user(name: str, plain: str) -> User | None:
    """authenticate user <name> and <plain> password."""
    if not (user := lookup_user(name)):
        return None
    if not verify_password(plain, user.hash):
        return None
    return user


def create_access_token(data: dict, expires: timedelta | None = None):
    """return a JWT access token"""
    src = data.copy()
    now = datetime.now()
    if not expires:
        expires = timedelta(minutes=15)
    src.update({"exp": now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# --- CRUD passthrough stuff


def get_all() -> list[User]:
    return data.get_all()


def get_one(name: str) -> User:
    return data.get_one(name)


def create(user: User) -> User:
    return data.create(user)


def modify(name: str, user: User) -> User:
    return data.modify(name, user)


def delete(name: str) -> bool:
    return data.delete(name)
