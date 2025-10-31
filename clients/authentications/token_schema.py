from pydantic import BaseModel, Field


class CreateTokenRequestSchema(BaseModel):
    """
    JSON схема для аутетификации, и получения токена, в системе только один пользователь (admin/password123)
    """
    username: str
    password: str


class CreateTokenResponseSchema(BaseModel):
    """
    JSON схема полученного токена после аутентификации
    """
    token: str
