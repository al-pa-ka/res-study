from sqlalchemy import MetaData, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import ForeignKey

from src.database import Base
from src.models import User

metadata = MetaData()


class UsedRefreshToken(Base):
    metadata = metadata
    __tablename__ = 'UsedRefreshToken'
    token: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id)) 

