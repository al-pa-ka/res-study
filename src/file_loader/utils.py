from typing import Any, Type
from io import FileIO

from sqlalchemy_file.file import File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database import async_session
from src.models import User


class Image:
    file: File
    owner: User.id

    @classmethod 
    async def save(cls, user: User, file: FileIO) -> 'Image':
        """save file and return file url"""
        async with async_session() as session:
            instance = cls(file = file, owner = user.id)
            session.add(instance)
            await session.commit()
            return instance
        

async def get_model_instance_by_url(model: Type[Image], static_url: str, session: None | AsyncSession = None):
    async def _get_model_instance_by_url(model: Type[Image], static_url: str, session: AsyncSession):
        select_statement = select(model).where(
            model.file.contains(static_url.split('/')[-1])
        )
        return await session.scalar(select_statement)
    
    if session:
        return await _get_model_instance_by_url(model, static_url, session)
    
    async with async_session() as session:
        return await _get_model_instance_by_url(model, static_url, session)