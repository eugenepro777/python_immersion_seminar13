"""
Задание №1.
    Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
    Обрабатывайте не числовые данные как исключения.
"""


# def request_number():
#     while True:
#         try:
#             number = float(input("Введите число: "))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                   f'Попробуйте снова')
#     return number

def request():
    while True:
        num = input("Введите число: ")
        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except ValueError as e:
                print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                      f'Попробуйте снова')


if __name__ == '__main__':
    number = request()
    print(f'Вы ввели число: {number}')
