from data.init import curs, conn, IntegrityError
from model.explorer import Explorer
from error import MissingError, DuplicateError


curs.execute(
    """create table if not exists explorer(
               name text primary key
             , country text
             , description text)"""
)


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(name=name, country=country, description=description)


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()


def get_one(name: str) -> Explorer:
    qry = """select * from explorer where name=:name"""
    params = {"name": name}
    curs.execute(qry, params)
    if row := curs.fetchone():
        return row_to_model(row)
    else:
        raise MissingError(msg=f"Explorer {name} not found.")


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(explorer: Explorer) -> Explorer:
    qry = """insert into explorer (name, country, description)
            values (:name, :country, :description)"""
    params = model_to_dict(explorer)

    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise DuplicateError(msg=f"Explorer {explorer.name} already exists.")
    return get_one(explorer.name)


def modify(explorer: Explorer) -> Explorer:
    qry = """update explorer
            set country=:country
                , name=:name
                , description=:description
            where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise MissingError(msg=f"Explorer {explorer.name} not found.")


def replace(explorer: Explorer) -> Explorer:
    return modify(explorer)


def delete(name: str) -> bool:
    qry = """delete from explorer where name = :name"""
    params = {"name": name}
    result = curs.execute(qry, params)
    if curs.rowcount != 1:
        raise MissingError(msg=f"Explorer {name} not found.")
    return bool(result)
