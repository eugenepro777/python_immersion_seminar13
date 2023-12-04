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

    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.level}\n'


user_group = set()
def load_users(path):
    with open(path, 'r', encoding='utf-8') as j_file:
        user_dict = json.load(j_file)
    for level, user_list in user_dict.items():
        for user_id, name in user_list.items():
            user_group.add(User(name, user_id, level))


if __name__ == '__main__':
    load_users('user_data.json')
    print(*user_group)
