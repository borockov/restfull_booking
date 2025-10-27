from httpx import Client

def get_public_http_builder() -> Client:
    return Client(timeout=100, base_url="https://restful-booker.herokuapp.com")
