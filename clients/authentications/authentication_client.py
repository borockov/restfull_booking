from httpx import Response

from clients.api_client import APIClient
from clients.authentications.token_schema import CreateTokenRequestSchema, CreateTokenResponseSchema
from clients.public_http_builder import get_public_http_builder
import allure


class AuthenticationClient(APIClient):
    @allure.step("Get Token")
    def auth(self, request: CreateTokenRequestSchema) -> Response:
        return self.post("https://restful-booker.herokuapp.com/auth", json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_builder())
