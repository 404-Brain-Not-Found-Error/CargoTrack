from passlib.hash import argon2
import asyncio

fast_argon2 = argon2.using(
    time_cost=2,
    memory_cost=51200,
)

def hash_password(password: str):
    return fast_argon2.hash(password)


def check_password(password: str, db_password: str) -> bool:
    return argon2.verify(password, db_password)
