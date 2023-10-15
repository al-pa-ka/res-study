from typing import Type

import pathlib

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker


PATH_TO_DATABASE = pathlib.Path(__file__).parent.parent.joinpath('./db.sqlite3').resolve()
DATABASE_URL = "sqlite+aiosqlite:///{}".format(PATH_TO_DATABASE).replace('\\', '/')


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


engine = create_async_engine(DATABASE_URL)
async_session: Type[AsyncSession] = sessionmaker(engine, class_=AsyncSession, autoflush=False, expire_on_commit=False)

