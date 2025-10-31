import logging


def get_logger(name: str) -> logging.Logger:
    # Инициализация логгера с указанным именем
    logger = logging.getLogger(name)
    # Устанавливаем уровень логирования DEBUG для логгера,
    # чтобы он обрабатывал все сообщения от DEBUG и выше
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger