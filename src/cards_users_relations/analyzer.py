import datetime
import time

from ..models import User
from ..cards.models import Course
from ..database import async_session
from ..cards.models import Card
from .schemes import Answer
from .models import UserAnswer


class AnswerProcessor:

    ONE_DAY = 60 * 60 * 24
    SIX_DAYS = ONE_DAY * 6

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def calculate_e_factor(self, answer: str, card: Card) -> int:
        if card.

    def calculate_next_time(self, answer: UserAnswer, e_factor: int, count_of_answers: int) -> datetime.datetime:
        current_unix_time = time.time()
        if count_of_answers == 1:
           days_to_repeat = self.ONE_DAY
        elif count_of_answers == 2:
            days_to_repeat = self.SIX_DAYS
        else:
            days_to_repeat = answer.e_factor * e_factor
        return datetime.datetime.fromtimestamp(current_unix_time + days_to_repeat)


    async def process_answer(self, answers: list[Answer]):
        async with async_session() as session:
            ...