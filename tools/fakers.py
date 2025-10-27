import random

from faker import Faker
from datetime import date, timedelta


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст
        :return: Случайный текст
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4
        :return: Случайный UUID%
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Генерирует предложение
        :return: Случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль
        :return: Случайный пароль
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует last_name
        :return: случайный last_name
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
          Генерирует first_name
          :return: случайный first_name
          """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
          Генерирует first_name
          :return: случайный first_name
          """
        return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное число от 1 до 100
        :return: От 1 до 100
        """
        return self.faker.random_int(start, end)

    def estimated_time(self) -> str:
        """
        Генерирует время прохождение курса на основе функции integer
        :return: Время прохождения курса
        """
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        """
        Генерирует максимальный бал от 50 до 100
        :return: От 50 до 100
        """
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        """
        Генерирует минимальный бал от 1 до 30
        :return: от 1 до 30
        """
        return self.integer(start=1, end=30)

    def date(self, start_year: int = 2018, end_year: int = 2025) -> str:
        """
        Генерирует случайную дату в формате 'YYYY-MM-DD'
        :param start_year: Начальный год для генерации
        :param end_year: Конечный год для генерации
        :return: Строка с датой 'YYYY-MM-DD'
        """
        start_date = date(start_year, 1, 1)
        end_date = date(end_year, 12, 31)
        delta_days = (end_date - start_date).days
        random_days = random.randint(0, delta_days)
        random_date = start_date + timedelta(days=random_days)
        return random_date.isoformat()  # вернёт в формате "YYYY-MM-DD"



fake = Fake(faker=Faker("ru_RU"))
