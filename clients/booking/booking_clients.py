from httpx import Response

from clients.api_client import APIClient
from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema, \
    UpdateBoookingRequestSchema, UpdateResponseBookingSchema


class BookingClient(APIClient):
    def get_booking_ids_api(self) -> Response:
        return self.get("https://restful-booker.herokuapp.com/booking")

    def get_booking(self, booking_id: str) -> Response:
        return self.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")

    def create_booking_api(self, request: CreateBookingRequestSchema) -> Response:
        return self.post("https://restful-booker.herokuapp.com/booking", json=request.model_dump(by_alias=True))

    def create_booking(self, request: CreateBookingRequestSchema) -> CreateBookingResponseSchema:
        response = self.create_booking_api(request)
        return CreateBookingResponseSchema.model_validate_json(response.text)

    def update_booking_api(self, booking_id: str, request: UpdateBoookingRequestSchema) -> Response:
        return self.put(f"https://restful-booker.herokuapp.com/booking/{booking_id}", json=request)

    def update_booking(self, booking_id: str, request: UpdateBoookingRequestSchema) -> UpdateResponseBookingSchema:
        response = self.update_booking_api(booking_id, request)
        return UpdateResponseBookingSchema.model_validate_json(response.text)

    def partial_update_booking_api(self, booking_id: str, request: UpdateBoookingRequestSchema) -> Response:
        return self.put(f"https://restful-booker.herokuapp.com/booking/{booking_id}", json=request)

    def partial_update_booking(self, booking_id: str,
                               request: UpdateBoookingRequestSchema) -> UpdateResponseBookingSchema:
        response = self.partial_update_booking_api(booking_id, request)
        return UpdateResponseBookingSchema.model_validate_json(response.text)
