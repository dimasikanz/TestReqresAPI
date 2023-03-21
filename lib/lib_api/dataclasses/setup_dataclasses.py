from dataclasses import dataclass


@dataclass
class NewAccountData:
    email: str
    password: str
    id: str
    token: str


@dataclass
class NewUserData:
    name: str
    job: str
    id: str
