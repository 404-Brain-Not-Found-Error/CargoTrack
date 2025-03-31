from fastapi import Depends, HTTPException, status

from repositories.users import UserRepository
from schemas.users import UserSchema
from utils.hash import hash_password


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
