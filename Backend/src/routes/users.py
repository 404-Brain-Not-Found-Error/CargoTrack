from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from repositories.users import UserRepository
from schemas.users import TokenResponseSchema, UserSchema
from services.users import UserService

router = APIRouter(prefix="/auth")


@router.post("/user/registration")
async def user_registration(
    user_data: UserSchema, db: AsyncSession = Depends(get_session)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    return await user_service.register_user(user_data.dict())


@router.post("/user/login")
async def user_login(user_data: UserSchema, response: Response, db: AsyncSession = Depends(get_session)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    token = await user_service.login_user(
        email=user_data.email, password=user_data.password
    )
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=7 * 24 * 3600,
        path="/",
    )

    return {"status", "OK"}