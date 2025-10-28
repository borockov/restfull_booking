from clients.booking.public_clients import get_public_http_client
from clients.booking.private_clients import get_private_http_client
from clients.booking.booking_schema import CreateBookingRequestSchema, UpdateBoookingRequestSchema


def clients_flow():
    public_client = get_public_http_client()
    private_clients = get_private_http_client()
    get_id = public_client.get_booking_ids_api()
    print(get_id.json())
    print('Все брони')

    get_booking = public_client.get_booking(47)
    print(get_booking.json())
    print('Конкретная бронь')

    create_booking_request = CreateBookingRequestSchema()
    create_booking_response = public_client.create_booking(create_booking_request)
    print(create_booking_response)
    print('Бронирование создано')
    print(create_booking_response.booking_id)

    update_booking_request = UpdateBoookingRequestSchema()
    update_booking = private_clients.update_booking_api(create_booking_response.booking_id, update_booking_request)
    print(update_booking.json())
    print('Обновление бронирования')

    update_booking_patch_request = UpdateBoookingRequestSchema(
        firstname='Tima',
        lastname='Borokov'
    )

    patch_booking = private_clients.partial_update_booking_api(create_booking_response.booking_id,
                                                               update_booking_patch_request)
    print(patch_booking.json())


if __name__ == "__main__":
    clients_flow()
