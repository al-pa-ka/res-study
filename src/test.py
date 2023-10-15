from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import async_session
from models import User

from asyncio import run





async def test():
    async with async_session() as session:
        user = User(
            name="Алексей", 
            surname="Полянин", 
            email="polyanin.04@mail.ru",
            login="alpaka",
            password="poolya333",
        )
        session.add(user)
        await session.commit()
        print(user.id)
        await session.close()

async def test_get():
    async with async_session() as session:
        selection = select(User).where(User.login == 'alpaka')#, User.password == 'poolya333')
        print(selection)
        users = await session.scalar(selection)
        await session.close()
        print(users)
        print(users.password == 'poolya333')

run(test())
run(test_get())