from httpx import Client
from clients.event_hooks import curl_event_hook

def get_public_http_builder() -> Client:
    return Client(timeout=100, base_url="https://restful-booker.herokuapp.com", event_hooks={"request": [curl_event_hook]})
