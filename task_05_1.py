import json



"""
Задание №5.
    Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
    - загрузка данных (функция из задания 4)
    - вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
    - добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""


class BasedExcep(Exception):
    pass


class NameErr(BasedExcep):
    pass


class LevelErr(BasedExcep):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка уровня"


class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level


class CheckUserLogin:
    users = []

    @staticmethod
    def create_user(name, user_id, level):
        try:
            if level > 3:
                raise LevelErr(level)
        except LevelErr as e:
            print(e)
        else:
            obj = User(name, user_id, level)
            CheckUserLogin.users.append(obj)

    @staticmethod
    def load_users():
        with open('user_data.json', 'r', encoding='UTF-8') as js_f:
            user_dict = json.load(js_f)
            for level, user_list in user_dict.items():
                for user_id, name in user_list.items():
                    CheckUserLogin.users.append(User(name, user_id, level))

    @staticmethod
    def get_login_level(name):
        try:
            for el in CheckUserLogin.users:
                if name == el.name:
                    return f'Пользователь найден'
                raise NameErr()
        except NameErr as e:
            return f"Пользователь не найден"


if __name__ == '__main__':
    user1 = CheckUserLogin()
    user1.load_users()
    print(len(user1.users))
    user1.create_user('Ivanov', '08', 2)
    print(user1.get_login_level('Новиков'))
