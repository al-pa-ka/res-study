import jwt
import time

from pydantic import BaseModel

from ..config import config

class Tokens(BaseModel):
    access_token: str
    refresh_token: str

    @classmethod
    def new(cls, user_id: int) -> 'Tokens':

        access_token = jwt.encode(
            {
                'user_id': user_id,
                'exp': int(time.time() + 60 * 30),
                'destination': 'access'
            },
            
            key=config.secret
        )

        refresh_token = jwt.encode(
            {
                'user_id': user_id,
                'exp': int(time.time() + 60 * 60 * 24 * 10),
                'destination': 'refresh'
            },

            key=config.secret
        )

        return cls(access_token=access_token, refresh_token=refresh_token)

