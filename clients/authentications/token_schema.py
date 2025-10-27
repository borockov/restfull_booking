from pydantic import BaseModel, Field


class CreateTokenRequestSchema(BaseModel):
    username: str
    password: str


class CreateTokenResponseSchema(BaseModel):
    token: str
