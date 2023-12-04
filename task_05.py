import json
from task_04 import User
from task_03 import UserAccessException, UserLevelException

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


class Project:
    def __init__(self):
        self.users = set()

    def load_data(self):
        self.users = User.load_user_data()

    def verification_login(self, name, user_id):
        login = User(name, user_id, 0)
        if login not in self.users:
            raise UserAccessException('Пользователь не найден')

        for user in self.users:
            if user == login:
                return user.access_level

    def add_user(self, name, user_id, access_level):
        new_user = User(name, user_id, access_level)
        for user in self.users:
            if user == new_user and user.access_level < access_level:
                raise UserLevelException('Вы не можете добавить пользователя с таким уровнем доступа')
        self.users.add(new_user)
        self._update_json_file()

    def _update_json_file(self):
        user_data = {}
        for user in self.users:
            if user.access_level not in user_data:
                user_data[user.access_level] = {}
            user_data[user.access_level][user.user_id] = user.name
        with open('user_data.json', 'w', encoding='utf-8') as j_file:
            json.dump(user_data, j_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    project = Project()
    project.load_data()

    # try:
    #     access_level = project.verification_login('User1', '123')
    #     print(f'Успешный вход. Уровень доступа: {access_level}')
    # except UserAccessException as e:
    #     print(f'В доступе отказано. {e}')

    # try:
    #     access_level = project.verification_login('Олег', '234')
    #     print(f'Успешный вход. Уровень доступа: {access_level}')
    # except UserAccessException as e:
    #     print(f'В доступе отказано. {e}')

    try:
        project.add_user('New_user', '256', 1)
        print('Пользователь успешно добавлен')
    except UserLevelException as e:
        print(f'Невозможно добавить пользователя. {e}')