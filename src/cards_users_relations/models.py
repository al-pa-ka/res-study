import datetime
import enum

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import TIMESTAMP, Enum

from ..database import Base
from ..models import User
from ..cards.models import Course, Deck, Card


class UserCourseRelation(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    course_id: Mapped[int] = mapped_column(ForeignKey(Course.id))


class UserAnswer(Base):

    class Marks(enum.Enum):
        PERFECT_RESPONSE = 5
        CORRECT_RESPONSE_AFTER_A_HESITATION = 4
        CORRECT_RESPONSE_AFTER_WITH_DIFFICULTY = 3
        INCORRECT_RESPONSE_SEEMED_EASY_TO_RECALL = 2
        INCORRECT_RESPONSE_CORRECT_ONE_REMEMBERED = 1
        COMPLETE_BLACKOUT = 0        

    card_id: Mapped[int] = mapped_column(ForeignKey(Card.id))
    answer: Mapped[str]
    answered_at: Mapped[datetime.datetime] = mapped_column(compare=TIMESTAMP, default=datetime.datetime.utcnow)
    next_time: Mapped[datetime.datetime] = mapped_column(compare=TIMESTAMP)
    e_factor: Mapped[str] = mapped_column(Enum(Marks))
    count_of_answers: Mapped[int]
