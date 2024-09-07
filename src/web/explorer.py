from fastapi import APIRouter, HTTPException, status
from model.explorer import Explorer
from error import DuplicateError, MissingError

# double/fake for testing
import os
if os.environ.get("CRYPTID_UNIT_TEST", ""):
    from fake import explorer as service
else:
    from service import explorer as service

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


@router.post("", status_code=status.HTTP_201_CREATED)
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except DuplicateError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.msg)


@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    try:
        return service.replace(explorer)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


@router.delete("/{name}")
def delete(name: str) -> bool:
    try:
        return service.delete(name)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)
