from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from ..auth.dependencies import get_user_by_token
from ..models import User
from .schemes import Card, Deck, Course
from .service import CourseCreator

router = APIRouter(prefix='/cards')


@router.post('/create_course')
async def create_course(course: Course, user: Annotated[User, Depends(get_user_by_token)]): 
    creator = CourseCreator(user)
    course = await creator.create_course(course)
    return course.id


# @router.get('/get_course')
# async def get_course(): ...

# @router.post('/update_deck')
# async def update_deck(): ...

# @router.post('/update_course')
# async def update_course(): ...

