from fastapi import APIRouter, HTTPException
from model.creature import Creature
import service.creature as service
from error import MissingError, DuplicateError


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
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except DuplicateError as exc:
        raise HTTPException(status_code=400, detail=exc.msg)


@router.patch("/")
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.put("/")
def replace(creature: Creature) -> Creature:
    try:
        return service.replace(creature)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{name}")
def delete(name: str) -> bool:
    try:
        return service.delete(name)
    except MissingError as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
