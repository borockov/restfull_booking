from httpx import Response

from clients.api_client import APIClient
from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema, \
    UpdateBoookingRequestSchema, UpdateResponseBookingSchema
from clients.private_http_builder import get_private_http_builder
from tools.routes import APIRoutes
import allure


class PrivateBookingClient(APIClient):
    @allure.step("Update Booking by {booking_id}")
    def update_booking_api(self, booking_id: str, request: UpdateBoookingRequestSchema) -> Response:
        """
        Приватный клиент для обновления номера
        :param booking_id: идентификатор забронированного номера
        :param request: Запрос на обновление номера
        :return: Возвращает объект Response с данными ответа
        """
        return self.put(f"{APIRoutes.BOOKING}/{booking_id}", json=request.model_dump(by_alias=True))

    def update_booking(self, booking_id: str, request: UpdateBoookingRequestSchema) -> UpdateResponseBookingSchema:
        """
        Клиент, который возвращает нам ответ в UpdateResponseBookingSchema после обновления бронирования
        :param booking_id: идентификатор забронированного номера
        :param request: Запрос на обновление номера
        :return: Возвращает ответ в виде json схемы UpdateResponseBookingSchema
        распарсит ответ от update_booking_api
        """
        response = self.update_booking_api(booking_id, request)
        return UpdateResponseBookingSchema.model_validate_json(response.text)

    @allure.step("Part Update by {booking_id}")
    def partial_update_booking_api(self, booking_id: str, request: UpdateBoookingRequestSchema) -> Response:
        """
        Клиент для частичного обновления забронированного номера
        :param booking_id: идентификатор забронированного номера
        :param request: Запрос для обновления номера
        :return: Возвращает объект Response
        """
        return self.patch(f"{APIRoutes.BOOKING}/{booking_id}", json=request.model_dump(by_alias=True))

    def partial_update_booking(self, booking_id: str,
                               request: UpdateBoookingRequestSchema) -> UpdateResponseBookingSchema:
        """
        Клиент, который возвращает нам ответ в UpdateResponseBookingSchema после обновления бронирования
         :param booking_id: идентификатор забронированного номера
        :param request: Запрос для обновления номера
         :return: Возвращает ответ в виде json схемы UpdateResponseBookingSchema
        распарсит ответ от update_booking_api
        """
        response = self.partial_update_booking_api(booking_id, request)
        return UpdateResponseBookingSchema.model_validate_json(response.text)

    @allure.step("Delete Booking by {booking_id}")
    def delete_booking(self, booking_id: str) -> Response:
        """
        Клиент для удаления бронирования
        :param booking_id: идентификатор бронирования
        :return: Возвращает объект Response
        """
        return self.delete(f"{APIRoutes.BOOKING}/{booking_id}")


def get_private_http_client() -> PrivateBookingClient:
    """
    Приватный билдер
    :return: Возвращает нам клиента PrivateBookingClient
    """
    return PrivateBookingClient(client=get_private_http_builder())
