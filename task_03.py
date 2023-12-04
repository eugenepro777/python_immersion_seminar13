"""
Задание №3.
    Создайте класс с базовым исключением и дочерние классы-исключения:
- ошибка уровня;
- ошибка доступа.
"""


# Сделали версию сразу с наполнением классов, другой вариант в задаче 6
class UserException(Exception):
    pass


class UserLevelException(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка уровня - level={self.value} меньше необходимого уровня)"


class UserAccessException(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка доступа"


if __name__ == '__main__':
    try:
        num = int(input("Введите целое число: "))
        if num < 1:
            raise UserAccessException(num)
        if num < 3:
            raise UserLevelException(num)
    except UserAccessException as e:
        print(e)
    except UserLevelException as e:
        print(e)
    else:
        print('Доступ есть')
    finally:
        print('Все хорошо')
