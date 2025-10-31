from enum import Enum


class APIRoutes(str, Enum):
    """
    Роутинги для uri
    """
    AUTH = "/auth"
    BOOKING = "/booking"

    def __str__(self):
        return self.value
