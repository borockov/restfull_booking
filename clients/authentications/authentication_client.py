from httpx import Response

from clients.api_client import APIClient
from clients.authentications.token_schema import CreateTokenRequestSchema, CreateTokenResponseSchema
from clients.public_http_builder import get_public_http_builder
from tools.routes import APIRoutes
import allure


class AuthenticationClient(APIClient):
    @allure.step("Get Token")
    def auth(self, request: CreateTokenRequestSchema) -> Response:
        """
        Клиент для аутентификации
        :param request: Принимает запрос на создание токена
        :return: Объект Response с ответом
        """
        return self.post(APIRoutes.AUTH, json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    """
    Подключение публичного билдера
    :return: возвращает объект AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_builder())
