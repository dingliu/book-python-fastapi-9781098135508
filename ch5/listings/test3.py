# test 3 for Pydantic data validation
from pydantic import BaseModel, Field


class Creature(BaseModel):
    name: str = Field(..., min_length=2)
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
