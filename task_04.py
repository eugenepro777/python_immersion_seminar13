import json
"""
Задание №4.
    Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
    Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
    Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""


class User:
    """"""
    MIN_ACCESS_LEVEL = 1
    MAX_ACCESS_LEVEL = 7

    def __init__(self, name, user_id, access_level):
        """Constructor for User"""
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.access_level}'

    def create_user_data_json(self):
        try:
            with open('user_data.json', 'r', encoding='utf-8') as j_file:
                user_data = json.load(j_file)
        except FileNotFoundError:
            print('Файл не найден')
            user_data = {}

        while True:
            self.name = input('Введите имя или exit для выхода: ')
            if self.name.lower().strip() == 'exit':
                break

            self.user_id = input('Введите личный идентификатор (ID): ')
            self.access_level = input(
                f'Введите уровень доступа (от {User.MIN_ACCESS_LEVEL} до {User.MAX_ACCESS_LEVEL}): ')
            while self.user_id in user_data.values():
                print('Пользователь с таким ID уже существует. Попробуйте другой')
                self.user_id = input('Введите личный идентификатор (ID): ')

            if self.access_level not in user_data:
                user_data[self.access_level] = {}
            while self.user_id in user_data[self.access_level]:
                print("ID пользователя для этого уровня доступа уже существует. Попробуйте другой")
                self.user_id = input('Введите личный идентификатор (ID): ')

            user_data[self.access_level][self.user_id] = self.name

        with open('user_data.json', 'w', encoding='utf-8') as j_file:
            json.dump(user_data, j_file, ensure_ascii=False, indent=2)

        print('Данные записаны')

    @staticmethod
    def load_user_data():
        try:
            with open('user_data.json', 'r', encoding='utf-8') as j_file:
                user_data = json.load(j_file)
        except FileNotFoundError:
            print('Файл не найден')
            return set()

        users = set()

        for access_level, user_id_name in user_data.items():
            for user_id, name in user_id_name.items():
                user = User(name, user_id, int(access_level))
                users.add(user)
        return users

    # к следующей задаче
    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)


if __name__ == '__main__':

    # создание файла с пользователями, раскомментировать если надо добавлять пользователя в файл или файла еще нет
    # new_user = User('', '', '')
    # new_user.create_user_data_json()

    # выводим список пользователей из файла
    existing_users = User.load_user_data()
    print("Существующие пользователи:")
    for user in existing_users:
        print(f"Name: {user.name}, ID: {user.user_id}, Access Level: {user.access_level}")

