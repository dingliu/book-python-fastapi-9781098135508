# test Pydantic data validation
from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated


class Creature(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2)]
    country: str
    area: str
    description: str
    aka: str


bad_creature = Creature(
    name="!",
    country="*",
    description="it's a raccoon",
    area="your attic",
    aka="Rocket",
)
