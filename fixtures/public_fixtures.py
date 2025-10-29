import pytest
from clients.booking.public_clients import get_public_http_client
from clients.booking.booking_schema import UpdateBoookingRequestSchema, CreateBookingRequestSchema

@pytest.fixture(scope="class")
def public_client():
    return get_public_http_client()


@pytest.fixture
def create_booking_request():
    return CreateBookingRequestSchema()


@pytest.fixture
def update_booking_request():
    return UpdateBoookingRequestSchema()