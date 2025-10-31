from httpx import Client
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
def get_public_http_builder() -> Client:
    """
    Публичный билдер, готовит данные для публичных клиентов
    :return:
    """
    return Client(
        timeout=100,
        base_url="https://restful-booker.herokuapp.com",
        event_hooks={"request": [curl_event_hook, log_request_event_hook],
                     "response":[log_response_event_hook]
                     })
