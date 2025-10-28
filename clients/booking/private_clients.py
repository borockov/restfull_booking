from httpx import Response

from clients.api_client import APIClient
from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema, \
    UpdateBoookingRequestSchema, UpdateResponseBookingSchema
from clients.private_http_builder import get_private_http_builder


class PrivateBookingClient(APIClient):

    def update_booking_api(self, booking_id: str, request: UpdateBoookingRequestSchema) -> Response:
        return self.put(f"/booking/{booking_id}", json=request.model_dump(by_alias=True))

    def update_booking(self, booking_id: str, request: UpdateBoookingRequestSchema) -> UpdateResponseBookingSchema:
        response = self.update_booking_api(booking_id, request)
        return UpdateResponseBookingSchema.model_validate_json(response.text)

    def partial_update_booking_api(self, booking_id: str, request: UpdateBoookingRequestSchema) -> Response:
        return self.put(f"/booking/{booking_id}", json=request.model_dump(by_alias=True))

    def partial_update_booking(self, booking_id: str,
                               request: UpdateBoookingRequestSchema) -> UpdateResponseBookingSchema:
        response = self.partial_update_booking_api(booking_id, request)
        return UpdateResponseBookingSchema.model_validate_json(response.text)

    def delete_booking(self, booking_id: str) -> Response:
        return self.delete(f"/booking/{booking_id}")


def get_private_http_client() -> PrivateBookingClient:
    return PrivateBookingClient(client=get_private_http_builder())
