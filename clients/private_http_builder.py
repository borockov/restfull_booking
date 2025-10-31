from functools import lru_cache
from httpx import Client
from clients.authentications.authentication_client import get_authentication_client
from clients.authentications.token_schema import CreateTokenRequestSchema
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook


@lru_cache(maxsize=None)
def get_private_http_builder() -> Client:
    """
    Приватный билдер, что бы для каждого клиента каждый раз не передвавть
    аутентификационные данные, мы указываем их в билдере, а затем вызываем билдер
    для каждого приватного клиента, по итогу подготовка данных для клиента становится автоматизированной
    :return: Возвращает нам готового клинета
    """
    authentication_client = get_authentication_client()

    login_request = CreateTokenRequestSchema(username='admin', password="password123")
    login_response = authentication_client.auth(login_request)
    login_response_data = login_response.json()

    return Client(
        timeout=100,
        base_url="https://restful-booker.herokuapp.com",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        cookies={"token": login_response_data['token']},
        event_hooks={"request": [curl_event_hook, log_request_event_hook],
                     "response": [log_response_event_hook]
                     }
    )
