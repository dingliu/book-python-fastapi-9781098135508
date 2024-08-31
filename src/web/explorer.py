from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
from service import explorer as service
from error import DuplicateError, MissingError


router = APIRouter(prefix="/explorer")


@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Explorer | None:
    try:
        return service.get_one(name)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except DuplicateError as exc:
        raise HTTPException(status_code=400, detail=exc.msg)


@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    try:
        return service.replace(explorer)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{name}")
def delete(name: str) -> bool:
    try:
        return service.delete(name)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
