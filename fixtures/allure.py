import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True)
def save_allure_enviroment_file():
    """
    Фикстура для создания переменных окружения в allure отчете
    :return:
    """
    yield
    create_allure_environment_file()
