import pytest
from clients.booking.private_clients import get_private_http_client
from fixtures.public_fixtures import public_client


@pytest.fixture(scope="class")
def private_client():
    """
    Фикстура для приватного клинета, готовит все данные необходимые для работы с приватными клиентами
    :return: Возвращает нам готового клиента
    """
    return get_private_http_client()


@pytest.fixture
def booking_id(public_client):
    """
    Фикстура для получения id бронирования
    :param public_client: Передается публичный клиент
    :return: возвращает из списка всех id бронирований, самый первый
    """
    response = public_client.get_booking_ids_api()
    return response.json()[0]['bookingid']


@pytest.fixture
def existing_booking_id(public_client):
    """Возвращает ID существующего бронирования"""
    bookings = public_client.get_booking_ids_api().json()
    assert bookings, "Нет доступных бронирований для теста"
    return bookings[0]['bookingid']
