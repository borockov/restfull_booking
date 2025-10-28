import pytest
from clients.booking.public_clients import get_public_http_client
from clients.booking.private_clients import get_private_http_client
from http import HTTPStatus
from clients.booking.booking_schema import CreateBookingRequestSchema, CreateBookingResponseSchema, \
    UpdateBoookingRequestSchema, UpdateResponseBookingSchema


@pytest.mark.regressions
def test_get_booking():
    public_client = get_public_http_client()
    get_booking = public_client.get_booking_ids_api()
    assert get_booking.status_code == HTTPStatus.OK


@pytest.mark.regressions
def test_get_booking_id():
    public_client = get_public_http_client()
    get_booking = public_client.get_booking_ids_api()
    get_booking_id = public_client.get_booking(get_booking.json()[0]['bookingid'])

    assert get_booking_id.status_code == HTTPStatus.OK
    assert get_booking.status_code == HTTPStatus.OK


@pytest.mark.regressions
def test_create_booking():
    public_client = get_public_http_client()

    create_booking_request = CreateBookingRequestSchema()
    create_booking_response = public_client.create_booking_api(create_booking_request)

    assert create_booking_response.status_code == HTTPStatus.OK
    print(create_booking_response.json())


@pytest.mark.regressions
def test_update_booking():
    private_client = get_private_http_client()
    public_client = get_public_http_client()
    get_booking = public_client.get_booking_ids_api()

    update_booking_request = UpdateBoookingRequestSchema()
    update_booking_response = private_client.update_booking_api(get_booking.json()[0]['bookingid'],
                                                                update_booking_request)

    assert update_booking_response.status_code == HTTPStatus.OK
    print(update_booking_response.json())

@pytest.mark.regressions
def test_update_patch_booking():
    private_client = get_private_http_client()
    public_client = get_public_http_client()
    get_booking = public_client.get_booking_ids_api()

    update_booking_patch_request = UpdateBoookingRequestSchema(
        firstname="Tima",
        lastname="Borokov"
    )

    update_booking_patch_response = private_client.partial_update_booking_api(get_booking.json()[0]['bookingid'], update_booking_patch_request)

    assert update_booking_patch_response.status_code == HTTPStatus.OK
    print(update_booking_patch_response.json())

@pytest.mark.regressions
def test_delete_booking():
    private_client = get_private_http_client()
    public_client = get_public_http_client()
    get_booking = public_client.get_booking_ids_api()

    delete_booking = private_client.delete_booking(get_booking.json()[0]['bookingid'])
    assert delete_booking.status_code == 201