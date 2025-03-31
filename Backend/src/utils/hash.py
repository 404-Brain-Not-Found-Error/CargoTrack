from passlib.hash import argon2


def hash_password(password: str):
    return argon2.hash(password)


def check_password(password: str, db_password: str) -> bool:
    return argon2.verify(password, db_password)
