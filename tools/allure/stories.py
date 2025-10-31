from enum import Enum

"""
Описываем в ENUM стори (конкретные пользовательские сценарии)
"""

class AllureStories(str, Enum):
    LOGIN = "Login"

    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entity"
    UPDATE_ENTITY = "Update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"
