from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.users import UserModel


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_data: dict):
        new_user = UserModel(**user_data)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return {"status": "OK"}

    async def get_by_email(self, email: str):
        result = await self.db.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalar_one_or_none()
