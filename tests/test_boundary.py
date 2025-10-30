import pytest
import allure
from tools.assertions.base import assert_status_code
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from http import HTTPStatus
from allure_commons.types import Severity
from clients.booking.booking_schema import CreateBookingResponseSchema
from tools.assertions.schema import validate_json_schema

@pytest.mark.boundary
@pytest.mark.regressions
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.BOOKING)
class TestBoundary:
    @allure.title("Test Boundary")
    @allure.tag("boundary", "regressions")
    # @allure.story(AllureStories.CREATE_ENTITY)
    # @allure.severity(Severity.CRITICAL)
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
        response_data = CreateBookingResponseSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())
        assert_status_code(response.status_code, HTTPStatus.OK)
