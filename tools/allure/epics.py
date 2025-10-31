from enum import Enum

"""
Описываем в ENUM Эпики(глобальные процессы)
"""
class AllureEpic(str, Enum):
    LMS = "LMS service"
    BOOKING = "BOOKING service"
