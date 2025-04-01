from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from jose import jwt

from repositories.users import UserRepository
from utils.hash import hash_password, check_password
from core.config import settings


class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def register_user(self, user_data: dict):
        existing_user = await self.user_repo.get_by_email(user_data["email"])
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email is already registred",
            )

        user_data["password"] = hash_password(user_data["password"])
        return await self.user_repo.create(user_data)

    async def login_user(self, email: str, password: str):
        user = await self.user_repo.get_by_email(email)
        if not user or not check_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        return self._create_access_token(user.id)

    def _create_access_token(self, user_id: int) -> str:
        expires = datetime.utcnow() + timedelta(days=7)
        to_encode = {"sub": str(user_id), "exp": expires}
        return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
