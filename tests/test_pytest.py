import pytest
from tools.assertions.schema import validate_json_schema
from http import HTTPStatus
from clients.booking.booking_schema import (
    CreateBookingRequestSchema,
    CreateBookingResponseSchema,
    UpdateBoookingRequestSchema,
    UpdateResponseBookingSchema)

from tools.assertions.base import assert_status_code


@pytest.mark.regressions
class TestBooking:
    def test_get_booking(self, public_client):
        get_booking = public_client.get_booking_ids_api()
        assert_status_code(get_booking.status_code, HTTPStatus.OK)

    def test_get_booking_id(self, public_client):
        get_booking = public_client.get_booking_ids_api()
        get_booking_id = public_client.get_booking(get_booking.json()[0]['bookingid'])

        assert_status_code(get_booking_id.status_code, HTTPStatus.OK)
        assert_status_code(get_booking.status_code, HTTPStatus.OK)

    def test_create_booking(self, public_client, create_booking_request):
        create_booking_response = public_client.create_booking_api(create_booking_request)
        create_booking_response_data = CreateBookingResponseSchema.model_validate_json(create_booking_response.text)

        assert_status_code(create_booking_response.status_code, HTTPStatus.OK)
        validate_json_schema(create_booking_response.json(), create_booking_response_data.model_json_schema())

    def test_update_booking(self, public_client, private_client, update_booking_request, existing_booking_id):

        update_booking_response = private_client.update_booking_api(existing_booking_id,
                                                                    update_booking_request)
        update_booking_response_data = UpdateResponseBookingSchema.model_validate_json(update_booking_response.text)

        assert_status_code(update_booking_response.status_code, HTTPStatus.OK)
        validate_json_schema(update_booking_response.json(), update_booking_response_data.model_json_schema())


    @pytest.mark.parametrize(
        'firstname, lastname',
        [
            ("Tima","Borokov"),
            ("Артур", "Кунашев"),
            ("Asker", "Ivanov"),
        ],
        ids=["latin_names", "cyrillic_names", "common_names"]
    )
    def test_update_patch_booking(self, private_client, public_client, firstname, lastname):
        get_booking = public_client.get_booking_ids_api()

        update_booking_patch_request = UpdateBoookingRequestSchema(
            firstname="Tima",
            lastname="Borokov"
        )

        update_booking_patch_response = private_client.partial_update_booking_api(get_booking.json()[0]['bookingid'],
                                                                                  update_booking_patch_request)
        update_booking_patch_response_data = UpdateResponseBookingSchema.model_validate_json(
            update_booking_patch_response.text)

        assert_status_code(update_booking_patch_response.status_code, HTTPStatus.OK)
        validate_json_schema(update_booking_patch_response.json(),
                             update_booking_patch_response_data.model_json_schema())

    def test_delete_booking(self, public_client, private_client):
        get_booking = public_client.get_booking_ids_api()

        delete_booking = private_client.delete_booking(get_booking.json()[0]['bookingid'])
        assert_status_code(delete_booking.status_code, HTTPStatus.CREATED)
