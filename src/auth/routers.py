from typing import Annotated

from fastapi import HTTPException
from fastapi import APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import Depends

from .schemes import RegistrationData, RefreshToken
from .service import Authentificator, Registrator
from .service import TokenChecker
from .exceptions import UsedRefreshTokenException
from .responses import Tokens


router = APIRouter()


@router.post('/', response_model_exclude_none=True)
async def authentificate_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Tokens:
    user = await Authentificator(form_data).authentificate()
    if not user:
        raise HTTPException(400, detail='InvalidLoginData')
    return Tokens.new(user.id)


@router.post('/registration')
async def registrate_user(registration_data: RegistrationData) -> Tokens:
    try:
        user = await Registrator(registration_data).registrate()
        tokens = Tokens.new(user.id)
        print(tokens)
        return tokens
    except Exception as e:
        print(e)
        raise HTTPException(400, detail='InvalidRegistrationData')


@router.post('/refresh')
async def refresh_tokens(token: RefreshToken) -> Tokens:
    try:
        token_payload = await TokenChecker.check_refresh_token(token.token)
        await TokenChecker.save_token_in_db(token.token)
        return Tokens.new(token_payload['user_id'])
    except UsedRefreshTokenException as e:
        raise HTTPException(400, detail='UsedRefreshToken') from e
    except Exception as e:
        raise HTTPException(502, detail="Unhandled exceptions")
