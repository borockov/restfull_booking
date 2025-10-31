import allure
from typing import Any
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles
"""
Базовый API Клиент, тут описаны основные методы, которые используются в проекте
"""

class APIClient():
    def __init__(self, client: Client):
        """
        Конструктор класса, принимает client httpx
        :param client:
        """
        self.client = client

    @allure.step("Make POST request to {url}")
    def post(self,
             url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None) -> Response:
        """
        Данный метод описывает метод POST
        :param url: url адресс ендпоинта
        :param json: запрос в json
        :param data: application data
        :param files: при работе с файлами
        :return: возвращает объект Response с данными ответа
        """

        return self.client.post(url, json=json, data=data, files=files)

    # @allure.step("Make GET Request to {url}")
    def get(self,
            url: URL | str,
            params: QueryParams | None = None) -> Response:
        """
        Описывает метод GET
        :param url: адрес эндпоинта
        :param params: query параметры
        :return: возвращает объект Response с данными ответа
        """
        return self.client.get(url, params=params)

    @allure.step("Make PUT Request to {url}")
    def put(self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None) -> Response:
        """
        Описывает метод PUT
        :param url: адрес ендпоинта
        :param json: запрос в json
        :param data:
        :param files:
        :return: Возвращает объект Response с данными ответа
        """
        return self.client.put(url, json=json, data=data, files=files)

    @allure.step("Make PATCH Request to {url}")
    def patch(self, url: URL | str,
              json: Any | None = None,
              data: RequestData | None = None,
              files: RequestFiles | None = None) -> Response:
        """
        Описывает метод PATCH
        :param url: адрес эндпоинта
        :param json: запрос в json
        :param data:
        :param files:
        :return: Возвращает объект Response
        """
        return self.client.patch(url, json=json, data=data, files=files)

    @allure.step("Make DELETES Request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        описывает метод DELETE
        :param url: Адрес энпоинта
        :return: возвращает объект Response
        """
        return self.client.delete(url)
