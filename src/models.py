import datetime

from sqlalchemy import MetaData, TIMESTAMP, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import PasswordType

from .database import Base
from .database import async_session


metadata = MetaData()


class User(Base):
    __tablename__ = 'User'
    metadata = metadata
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    login: Mapped[str] = mapped_column(unique=True)
    password = Column(PasswordType(schemes=["md5_crypt", "sha256_crypt"]), nullable=False)
    confirmed: Mapped[bool] = mapped_column(default=False)
    registered_at: Mapped[datetime.datetime] = mapped_column(compare=TIMESTAMP, default=datetime.datetime.utcnow)

