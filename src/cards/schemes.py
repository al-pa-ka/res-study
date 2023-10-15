from typing import Optional, Literal
from abc import ABC

from pydantic import BaseModel, Field

from enum import IntEnum

from .utils import StaticUrl


class AccessModifierEnum(IntEnum):
    OPEN = 1
    CLOSED = 2


class Card(BaseModel): 
    question: str
    answer: str
    attachment: Optional[StaticUrl] = None
    id: Optional[int] = None


class Deck(BaseModel):
    title: str 
    cards: list[Card]
    cover: Optional[StaticUrl] = None
    id: Optional[int] = None


class Course(BaseModel):
    access: AccessModifierEnum = Field(AccessModifierEnum.OPEN, alias='access_modifier')
    title: Optional[str]
    decks: list[Deck]
    cover: Optional[StaticUrl] = None
    id: Optional[int] = None
