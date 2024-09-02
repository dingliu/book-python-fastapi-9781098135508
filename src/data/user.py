from model.user import User
from data.init import conn, curs, get_db, IntegrityError
from error import MissingError, DuplicateError


curs.execute(
    """create table if not exists user(
             name text primary key
             , hash text)"""
)


curs.execute(
    """create table if not exists xuser(
             name text primary key
             , hash text)"""
)


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(name=name, hash=hash)


def model_to_dict(user: User) -> dict:
    return user.model_dump()


def get_one(name: str) -> User:
    qry = """select * from user where name:=name"""
    params = {"name": name}
    curs.execute(qry, params)
    if row := curs.fetchone():
        return row_to_model(row)
    else:
        raise MissingError(msg=f"User {name} not found.")


def get_all() -> list[User]:
    qry = """select * from user"""
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(user: User, table: str = "user"):
    """Add <user> to user or xuser table"""
    qry = f"""insert into {table} (user, hash)
              values (:name, :hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise DuplicateError(msg=f"{table}: user {user.name} already exists.")


def modify(name: str, user: User) -> User:
    qry = """update user set
            name=:name, hash=:hash
            where name=:name_orig"""
    params = {"name": user.name, "hash": user.hash, "name_orig": name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(user.name)
    else:
        raise MissingError(msg=f"User {name} not found.")


def delete(name: str) -> bool:
    """Drop user with <name> from user table, add to xuser table."""
    user = get_one(name)
    qry = """delete from user where name = :name"""
    params = {"name": name}
    result = curs.execute(qry, params)
    if curs.rowcount != 1:
        raise MissingError(msg=f"User {name} not found.")
    else:
        create(user, "xuser")
        return bool(result)
