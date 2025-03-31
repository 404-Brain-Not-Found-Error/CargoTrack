from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from repositories.users import UserRepository
from schemas.users import UserSchema
from services.users import UserService

router = APIRouter(prefix="/auth")


@router.post("/user/registration")
async def user_registration(
    user_data: UserSchema, db: AsyncSession = Depends(get_session)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    return await user_service.register_user(user_data.dict())
