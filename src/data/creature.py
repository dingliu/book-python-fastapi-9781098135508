from data.init import conn, curs, IntegrityError
from model.creature import Creature
from error import MissingError, DuplicateError


curs.execute(
    """create table if not exists creature(
               name text primary key
             , description text
             , country text
             , area text
             , aka text)"""
)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name, country=country, area=area, description=description, aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    if row := curs.fetchone():
        return row_to_model(row)
    else:
        raise MissingError(msg=f"Creature {name} not found.")


def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature):
    qry = """insert into creature values
          (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise DuplicateError(msg=f"Creature {creature.name} already exists.")
    return get_one(creature.name)


def modify(creature: Creature) -> Creature:
    qry = """update creature
            set country=:country
                , name=:name
                , description=:description
                , area=:area
                , aka=:aka
            where name=:name_orig"""
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise MissingError(msg=f"Creature {creature.name} not found.")


def replace(creature: Creature) -> Creature:
    return modify(creature)


def delete(name: str) -> bool:
    qry = "delete from creature where name = :name"
    params = {"name": name}
    result = curs.execute(qry, params)
    if curs.rowcount != 1:
        raise MissingError(msg=f"Creature {name} not found.")
    return bool(result)
