# define a subrouter dependency
from fastapi import FastAPI, Depends, APIRouter


# dependency function
def dep_func():
    pass


router = APIRouter(dependencies=[Depends(dep_func)])
