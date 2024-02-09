from pydantic import BaseModel, Field
from random import randint, choice
from string import ascii_letters, digits

PASSWORD_FROM_TO = [6, 50]


def create_password():
    password_length = randint(PASSWORD_FROM_TO[0], PASSWORD_FROM_TO[1])
    symbols = ascii_letters + digits
    new_password = ''
    for _ in range(password_length):
        new_password += choice(symbols)
    return new_password


class UserIn(BaseModel):
    firstname: str = Field(..., max_length=32)
    lastname: str = Field(..., max_length=64)
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=PASSWORD_FROM_TO[0], max_length=PASSWORD_FROM_TO[1])


class User(UserIn):
    id: int

