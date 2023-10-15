import jwt
from typing import Annotated
from sqlalchemy import select

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException

from src.models import User
from src.database import async_session
from src.config import config

oauth = OAuth2PasswordBearer('/auth/')


def get_token_by_authorization_header(token: Annotated[str, oauth]) -> dict:
    try:
        token = jwt.decode(token, config.secret, ('HS256',))
        if token['destination'] != 'access':
            raise Exception
        return token
    except Exception as e:
        raise HTTPException(400, "Invalid token") from e
    

async def get_user_by_token(token: Annotated[dict, Depends(get_token_by_authorization_header)]) -> User:
    async with async_session() as session:
        user_id = token['user_id']
        select_statement = select(User).where(User.id == user_id)
        user = await session.scalar(select_statement)
        if not user:
            raise Exception('User was deleted')
        return user
