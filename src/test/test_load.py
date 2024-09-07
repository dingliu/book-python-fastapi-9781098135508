from faker import Faker
from time import perf_counter


def load():
    from error import DuplicateError
    from data.explorer import create
    from model.explorer import Explorer

    f = Faker()
    NUM = 100_000
    t1 = perf_counter()
    for row in range(NUM):
        try:
            create(Explorer(
                name=f.name(),
                country=f.country(),
                description=f.address()
            ))
        except DuplicateError:
            pass # Faker can generate duplicated names
    t2 = perf_counter()
    print(NUM, "rows")
    print("write time:", str(t2 - t1))


def read_db():
    from data.explorer import get_all

    t1 = perf_counter()
    get_all()
    t2 = perf_counter()
    print("DB read time:", str(t2 - t1))


def read_api():
    from fastapi.testclient import TestClient
    from main import app

    t1 = perf_counter()
    client = TestClient(app)
    client.get("/explorer")
    t2 = perf_counter()
    print("API read time:", str(t2 - t1))


load()
read_db()
read_api()
