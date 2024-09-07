from fastapi import status, HTTPException


def assert_duplicate(e: HTTPException):
    assert e.status_code == status.HTTP_409_CONFLICT
    assert "Duplicate" in e.args


def assert_missing(e: HTTPException):
    assert e.status_code == status.HTTP_404_NOT_FOUND
    assert "Missing" in e.args
