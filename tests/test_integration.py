import allure
import pytest
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from clients.booking.booking_schema import UpdateBoookingRequestSchema
from allure_commons.types import Severity

@pytest.mark.regressions
@pytest.mark.integration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.BOOKING)
@allure.severity(Severity.NORMAL)
class TestIntegration:
    @allure.title("Booking Test Full Flow")
    @allure.tag("integrations", "regressions")
    @allure.story(AllureStories.CREATE_ENTITY)
    def test_booking_full_flow(self, public_client, private_client, create_booking_request, booking_id):
        update_request = UpdateBoookingRequestSchema(firstname="Updated", lastname="User")
        update_response = private_client.partial_update_booking_api(booking_id, update_request)

        assert_status_code(update_response.status_code, HTTPStatus.OK)

        get_response = public_client.get_booking(booking_id)
        assert get_response.json()['firstname'] == "Updated"

        delete_response = private_client.delete_booking(booking_id)
        assert_status_code(delete_response.status_code, HTTPStatus.CREATED)
