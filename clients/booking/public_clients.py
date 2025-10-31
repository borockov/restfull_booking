from clients.api_client import APIClient
from httpx import Response
from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema
from clients.public_http_builder import get_public_http_builder
from tools.routes import APIRoutes
import allure


class PublicBookingClients(APIClient):
    @allure.step("Get Booking IDS")
    def get_booking_ids_api(self) -> Response:
        """
        Клиент возвращает нам список всех бронирований в виде json
        :return: Возвращает объект Response со всеми бронированиями
        """
        return self.get(APIRoutes.BOOKING)

    @allure.step("Get Booking ID")
    def get_booking(self, booking_id: str) -> Response:
        """
        Возвращает нам бронирование по указанному id
        :param booking_id: идентификатор бронирования
        :return: Возвращает объект Response
        """
        return self.get(f"{APIRoutes.BOOKING}/{booking_id}")

    @allure.step("Create Booking")
    def create_booking_api(self, request: CreateBookingRequestSchema) -> Response:
        """
        Клиент для создания бронирования
        :param request: Принимает request Json модель
        :return: Возвращает объект Response с данными ответа
        """
        return self.post(APIRoutes.BOOKING, json=request.model_dump(by_alias=True))

    def create_booking(self, request: CreateBookingRequestSchema) -> CreateBookingResponseSchema:
        """
        Клиент возвращает нам объект CreateBookingResponseSchema (после успешного бронирования)
        :param request: запрос на бронирование
        :return: Возвращает CreateBookingResponseSchema
        Передает запрос на create_booking_api
        """
        response = self.create_booking_api(request)
        return CreateBookingResponseSchema.model_validate_json(response.text)


def get_public_http_client():
    """
    клиент для публчиного билдера
    :return: Возвращает нам PublicBookingClients
    """
    return PublicBookingClients(client=get_public_http_builder())
