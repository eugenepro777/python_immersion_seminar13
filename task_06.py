"""
Задание №6.
    Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
    Передавайте необходимые данные из основного кода
проекта.
"""


class UserException(Exception):
    pass


class UserLevelException(UserException):
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f"Ошибка уровня доступа: Нельзя добавить пользователя '{self.name}' с идентификатором '{self.user_id}'" \
               f" и уровнем доступа '{self.access_level}' из-за более высокого уровня доступа"


class UserAccessException(UserException):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Доступ запрещен. Пользователь '{self.name}' с идентификатором '{self.user_id}' не найден"