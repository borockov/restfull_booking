from functools import lru_cache
from httpx import Client
from clients.authentications.authentication_client import get_authentication_client
from clients.authentications.token_schema import CreateTokenRequestSchema

@lru_cache(maxsize=None)
def get_private_http_builder() -> Client:
    authentication_client = get_authentication_client()

    login_request = CreateTokenRequestSchema(username='admin', password="password123")
    login_response = authentication_client.auth(login_request)
    login_response_data = login_response.json()

    return Client(
        timeout=100,
        base_url="https://restful-booker.herokuapp.com",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        cookies={"token": login_response_data['token']}
    )

