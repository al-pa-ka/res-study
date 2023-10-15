from pydantic import BaseModel


class RegistrationData(BaseModel):
    name: str
    surname: str
    login: str
    email: str
    password: str

class RefreshToken(BaseModel):
    token: str