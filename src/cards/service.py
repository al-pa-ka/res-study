from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemes import Course as CourseScheme
from .schemes import Deck as DeckScheme
from .schemes import Card as CardScheme

from .models import Course, Deck, Card
from ..models import User
from ..file_loader.models import Cover, Attachment
from ..database import async_session
from ..file_loader.utils import get_model_instance_by_url


class CourseCreator:
    def __init__(self, user: User) -> None:
        self.user = user

    async def create_course(self, course: CourseScheme) -> Course:
        async with async_session() as session:
            course_payload = course.model_dump(by_alias=True)
            course_payload.pop('decks')
            course_payload['author'] = self.user.id
            course_payload['cover'] = await get_model_instance_by_url(
                Cover, course.cover, session
            ) if course.cover else None
            course_instance = Course(**course_payload)
            session.add(course_instance)
            await session.commit()
            for deck in course.decks:
                await self._create_deck(course_instance, deck, session)
            await session.commit()
            return course
            
    async def _create_deck(self, course: Course, deck: DeckScheme, session: AsyncSession):
        deck_payload = deck.model_dump()
        deck_payload['course'] = course.id
        deck_payload['cover'] = await get_model_instance_by_url(
            Cover, course.cover, session
        ) if course.cover else None
        cards = deck_payload.pop('cards')
        deck_instance = Deck(**deck_payload)
        session.add(deck_instance)
        await session.commit()
        for ordinal, card in enumerate(deck.cards):
            await self._create_card(deck_instance, card, ordinal, session) # add cards to session, but doesn't commit 

    async def _create_card(self, deck: Deck, card: CardScheme, ordinal: int, session: AsyncSession):
        card_payload = card.model_dump()
        card_payload['deck'] = deck.id
        card_payload['ordinal'] = ordinal
        card_payload['attachment'] = await get_model_instance_by_url(
            Attachment, card.attachment, session
        ) if card.attachment else None
        card = Card(**card_payload)
        session.add(card)


class Updater:
    def __init__(self, user: User):
        self.user = user
    
# class CourseGetter:
#     def __init__(self, user: User) -> None:
#         self.user = user

#     async def get_course_by_id(self, course_id: int):
#         ...

#     async def get_all_user_courses(self):
#         async with async_session() as session:
#             select_statement = select(Course).where(Course.author==self.user.id)


#     @staticmethod
#     async def get_popular_courses():
#         ...

    