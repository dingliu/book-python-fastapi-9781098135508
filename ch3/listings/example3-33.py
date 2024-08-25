# model variations
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, UTC


class TagIn(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

class TagOut(BaseModel):
    tag: str
    created: datetime

def save_tag(tag: Tag):
    ...

def load_tag(tag_str: str) -> Tag:
    ...

app = FastAPI()

@app.post("/")
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(UTC), secret="shhh")
    save_tag(tag)
    return tag_in

@app.get("/{tag_str}", response_model=TagOut)
def get(tag_str: str) -> TagOut:
    tag: Tag = load_tag(tag_str)
    return tag
