from dataclasses import dataclass

@dataclass
class NewUserData:
    email: str
    password: str
    id: str
    token: str