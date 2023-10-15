import datetime
import random
import string
from enum import IntEnum

from sqlalchemy import MetaData
from sqlalchemy import TIMESTAMP
from sqlalchemy.schema import ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base
from src.models import User
from src.file_loader.models import Cover, Attachment


metadata = MetaData()


class AccessModifier(Base):
    metadata = metadata
    __tablename__ = 'AccessModifier'
    name: Mapped[str]  #['open', 'closed'] may be extended 


class Course(Base):
    metadata = metadata
    __tablename__ = 'Course'
    author: Mapped[int] = mapped_column(ForeignKey(User.id))
    title: Mapped[str]
    cover: Mapped[int] = mapped_column(ForeignKey(Cover.id), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(compare=TIMESTAMP, default=datetime.datetime.utcnow)
    access_modifier: Mapped[int] = mapped_column(ForeignKey(AccessModifier.id))
    key: Mapped[str] = mapped_column(default=lambda: ''.join([random.choice(
        string.ascii_lowercase + string.ascii_uppercase + string.digits
    ) for _ in range(100)]))


class Deck(Base):
    metadata = metadata
    __tablename__ = 'Deck'
    course = Column(ForeignKey(Course.id))
    title: Mapped[str]
    cover: Mapped[int] = mapped_column(ForeignKey(Cover.id), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(compare=TIMESTAMP, default=datetime.datetime.utcnow)
    # author: Mapped[int] = mapped_column(ForeignKey(User.id), nullable=True) # if deck has no course
    # access_modifier: Mapped[int] = mapped_column(ForeignKey(AccessModifier.id), nullable=True) # ↑ same 
    # key: Mapped[str] = mapped_column(default=lambda: ''.join([random.choice(
    #     string.ascii_lowercase + string.ascii_uppercase + string.digits
    # ) for _ in range(100)]), nullable=True) # if deck has no course


class Card(Base):
    metadata = metadata
    __tablename__ = 'Card'
    question: Mapped[str]
    answer: Mapped[str]
    ordinal: Mapped[int]
    attachment: Mapped[int] = mapped_column(ForeignKey(Attachment.id), nullable=True)
    deck: Mapped[int] = mapped_column(ForeignKey(Deck.id))
    last_version: Mapped[int] = mapped_column(ForeignKey('Card.id'), nullable=True)
    is_hided: Mapped[bool] = mapped_column(default=False)
