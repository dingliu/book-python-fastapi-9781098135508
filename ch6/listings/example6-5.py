# define app level dependencies
from fastapi import FastAPI, Depends


def dep_func1():
    pass


def dep_func2():
    pass


app = FastAPI(dependencies=[Depends(dep_func1), Depends(dep_func2)])


@app.get("/hello")
def greet():
    pass
