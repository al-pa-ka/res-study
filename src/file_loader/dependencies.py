from fastapi import UploadFile
from sqlalchemy_file.file import File


async def to_sqlalchemy_file(file: UploadFile) -> File:
    return File(await file.read(), content_type=file.content_type)

