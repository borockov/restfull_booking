import allure
from typing import Any
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles


class APIClient():
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Make POST request to {url}")
    def post(self,
             url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    # @allure.step("Make GET Request to {url}")
    def get(self,
            url: URL | str,
            params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    @allure.step("Make PUT Request to {url}")
    def put(self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None) -> Response:
        return self.client.put(url, json=json, data=data, files=files)

    @allure.step("Make PATCH Request to {url}")
    def patch(self, url: URL | str,
              json: Any | None = None,
              data: RequestData | None = None,
              files: RequestFiles | None = None) -> Response:
        return self.client.patch(url, json=json, data=data, files=files)

    @allure.step("Make DELETES Request to {url}")
    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)
