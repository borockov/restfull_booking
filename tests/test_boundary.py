import pytest
from tools.assertions.base import assert_status_code
from http import HTTPStatus


@pytest.mark.boundary
@pytest.mark.regressions
class TestBoundary:
    @pytest.mark.parametrize(
        "total_price",
        [0, 1, 999999],
        ids=['zero_price', "min_price", "max_price"]
    )
    def test_create_booking_with_boundary_price(self, public_client, total_price, create_booking_request):
        create_request = {
            "firstname": "Flow",
            "lastname": "Test",
            "totalprice": 500,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-01",
                "checkout": "2025-01-10"
            },
            "additionalneeds": "Lunch"
        }
        response = public_client.create_booking_api(request=create_booking_request)
        assert_status_code(response.status_code, HTTPStatus.OK)
