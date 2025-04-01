from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=32,
    )


class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
