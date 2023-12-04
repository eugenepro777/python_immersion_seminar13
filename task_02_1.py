"""
Задание №2.
    Создайте функцию аналог get для словаря.
    Помимо самого словаря функция принимает ключ и
значение по умолчанию.
    При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
    Реализуйте работу через обработку исключений.
"""


def custom_get(dictionary, key, default_value=0):
    try:
        res = dictionary[key]
    except KeyError as e:
        print(f'Ключа {e} нет в словаре ')
        res = default_value
    return res


if __name__ == '__main__':
    my_dict = {"one": 'a', "two": 3, "three": [3, 5]}
    result1 = custom_get(my_dict, '1')
    result2 = custom_get(my_dict, 'three')
    print(result1)
    print(result2)
