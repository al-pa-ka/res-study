from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy_file.file import File

from src.models import User
from src.auth.dependencies import get_user_by_token
from .dependencies import to_sqlalchemy_file
from .models import Cover, UserIcon, Attachment


router = APIRouter(prefix='/file')


@router.post('/upload_attachment')
async def upload_attachment(user: Annotated[User, Depends(get_user_by_token)],
                            file: Annotated[File, Depends(to_sqlalchemy_file)]) -> str:
    saved_attachment = await Attachment.save(user=user, file=file)
    return '/static/{}'.format(saved_attachment.file['path'])

@router.post('/upload_user_icon')
async def upload_user_icon(user: Annotated[User, Depends(get_user_by_token)], 
                           file: Annotated[File, Depends(to_sqlalchemy_file)]) -> str:
    saved_icon = await UserIcon.save(user=user, file=file)
    return '/static/{}'.format(saved_icon.file['path'])

@router.post('/upload_cover')
async def upload_cover(user: Annotated[User, Depends(get_user_by_token)], 
                       file: Annotated[File, Depends(to_sqlalchemy_file)]) -> str:
    saved_cover = await Cover.save(user=user, file=file)
    return '/static/{}'.format(saved_cover.file['path'])
