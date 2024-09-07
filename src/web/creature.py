from fastapi import APIRouter, HTTPException, status
from model.creature import Creature
from error import MissingError, DuplicateError

# double/fake for testing
import os
if os.environ.get("CRYPTID_UNIT_TEST", ""):
    from fake import creature as service
else:
    import service.creature as service

router = APIRouter(prefix="/creature")


@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Creature | None:
    try:
        return service.get_one(name)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


@router.post("", status_code=status.HTTP_201_CREATED)
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except DuplicateError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.msg)


@router.patch("/")
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


@router.put("/")
def replace(creature: Creature) -> Creature:
    try:
        return service.replace(creature)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


@router.delete("/{name}")
def delete(name: str) -> bool:
    try:
        return service.delete(name)
    except MissingError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)
