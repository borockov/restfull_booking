import allure

@allure.step("Check status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус код.
    raise AssertionError: Если статус-коды не совпадают.
    """
    # logger.info(f"Check that response status code equals to {expected}")
    assert actual == expected, (
        'Неккоректный статус код'
        f'Ожидаемый статус {expected}'
        f'Полученный статус {actual}'
    )
