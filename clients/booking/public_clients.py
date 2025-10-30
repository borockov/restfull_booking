from clients.api_client import APIClient
from httpx import Response
from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema
from clients.public_http_builder import get_public_http_builder
import allure


class PublicBookingClients(APIClient):
    @allure.step("Get Booking IDS")
    def get_booking_ids_api(self) -> Response:
        return self.get("/booking")

    @allure.step("Get Booking ID")
    def get_booking(self, booking_id: str) -> Response:
        return self.get(f"/booking/{booking_id}")

    @allure.step("Create Booking")
    def create_booking_api(self, request: CreateBookingRequestSchema) -> Response:
        return self.post("/booking", json=request.model_dump(by_alias=True))

    def create_booking(self, request: CreateBookingRequestSchema) -> CreateBookingResponseSchema:
        response = self.create_booking_api(request)
        return CreateBookingResponseSchema.model_validate_json(response.text)


def get_public_http_client():
    return PublicBookingClients(client=get_public_http_builder())
