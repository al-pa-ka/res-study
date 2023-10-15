from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import jwt

from ..models import User
from ..database import async_session
from ..config import config

from .models import UsedRefreshToken
from .schemes import RegistrationData
from .responses import Tokens
from .exceptions import UsedRefreshTokenException


class Authentificator:
    def __init__(self, login_data: OAuth2PasswordRequestForm) -> None:
        self.login_data = login_data

    async def authentificate(self) -> User | None:
        user = await Authentificator.get_user(self.login_data.username)
        if user and self.check_password(user):
            return user
            
    @staticmethod
    async def get_user(login) -> User | None:
        async with async_session() as session:
            if '@' in login:
                select_statement = select(User).where(User.email==login)
            else:
                select_statement = select(User).where(User.login==login)

            results = await session.scalars(select_statement)
            return results.one_or_none()
        
    def check_password(self, user: User) -> bool:
        return user.password == self.login_data.password #passlib authohash


class Registrator:
    def __init__(self, registration_data: RegistrationData) -> None:
        self.registration_data = registration_data

    async def registrate(self) -> User:
        async with async_session() as session:
            print(self.registration_data.model_dump())
            user = User(**self.registration_data.model_dump())
            session.add(user)
            await session.commit()
            return user
        
class TokenChecker:
    @staticmethod
    async def check_refresh_token(token: str) -> dict:
        token_payload = jwt.decode(token, config.secret, algorithms=('HS256',))
        if token_payload['destination'] != 'refresh':
            raise Exception('InvalidToken')
        async with async_session() as session:
            select_statement = select(UsedRefreshToken).where(UsedRefreshToken.token==token)
            if await session.scalar(select_statement):
                raise UsedRefreshTokenException

        return token_payload
        
    @staticmethod 
    async def save_token_in_db(token: str):
        async with async_session() as session:
            token_payload = jwt.decode(token, config.secret, algorithms=('HS256',))
            token = UsedRefreshToken(token=token, user_id=token_payload['user_id'])
            session.add(token)
            await session.commit()