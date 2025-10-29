import pytest
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from clients.booking.booking_schema import UpdateBoookingRequestSchema


@pytest.mark.regressions
@pytest.mark.integration
class TestIntegration:
    def test_booking_full_flow(self, public_client, private_client, create_booking_request, booking_id):
        update_request = UpdateBoookingRequestSchema(firstname="Updated", lastname="User")
        update_response = private_client.partial_update_booking_api(booking_id, update_request)

        assert_status_code(update_response.status_code, HTTPStatus.OK)

        get_response = public_client.get_booking(booking_id)
        assert get_response.json()['firstname'] == "Updated"

        delete_response = private_client.delete_booking(booking_id)
        assert_status_code(delete_response.status_code, HTTPStatus.CREATED)
