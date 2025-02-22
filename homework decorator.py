import os
import datetime
from functools import wraps


# def logger(old_function):
#     @wraps(old_function)
#     def new_function(*args, **kwargs):
#         start_fun = datetime.datetime.now()
#         res = old_function(*args, **kwargs)
#         with open('main.log', 'a') as f:
#             f.write(
#                 f'''
#                 Время вызова функции - {start_fun},
#                 Имя функции - {old_function.__name__},
#                 Аргументы функции- {args} и {kwargs},
#                 Результат функции - {res}.'''
#             )
#         return res
#
#     return new_function


# def test_1():
#     path = 'main.log'
#     if os.path.exists(path):
#         os.remove(path)
#
#     @logger
#     def hello_world():
#         return 'Hello World'
#
#     @logger
#     def summator(a, b=0):
#         return a + b
#
#     @logger
#     def div(a, b):
#         return a / b
#
#     assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#     result = summator(2, 2)
#     assert isinstance(result, int), 'Должно вернуться целое число'
#     assert result == 4, '2 + 2 = 4'
#     result = div(6, 2)
#     assert result == 3, '6 / 2 = 3'
#
#     assert os.path.exists(path), 'файл main.log должен существовать'
#
#     summator(4.3, b=2.2)
#     summator(a=0, b=0)
#
#     with open(path) as log_file:
#         log_file_content = log_file.read()
#
#     assert 'summator' in log_file_content, 'должно записаться имя функции'
#     for item in (4.3, 2.2, 6.5):
#         assert str(item) in log_file_content, f'{item} должен быть записан в файл'


# if __name__ == '__main__':
#     test_1()


def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            start_fun = datetime.datetime.now().strftime('%H:%M:%S')
            res = old_function(*args, **kwargs)
            with open(path, 'a') as f:
                f.write(
                    f'''
                    Время вызова функции - {start_fun},
                    Имя функции - {old_function.__name__},
                    Аргументы функции- {args} и {kwargs},
                    Результат функции - {res}.'''
                )
            return res

        return new_function

    return __logger


# def test_2():
#     paths = ('log_1.log', 'log_2.log', 'log_3.log')
#
#     for path in paths:
#         if os.path.exists(path):
#             os.remove(path)
#
#         @logger(path)
#         def hello_world():
#             return 'Hello World'
#
#         @logger(path)
#         def summator(a, b=0):
#             return a + b
#
#         @logger(path)
#         def div(a, b):
#             return a / b
#
#         assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#         result = summator(2, 2)
#         assert isinstance(result, int), 'Должно вернуться целое число'
#         assert result == 4, '2 + 2 = 4'
#         result = div(6, 2)
#         assert result == 3, '6 / 2 = 3'
#         summator(4.3, b=2.2)
#
#     for path in paths:
#
#         assert os.path.exists(path), f'файл {path} должен существовать'
#
#         with open(path) as log_file:
#             log_file_content = log_file.read()
#
#         assert 'summator' in log_file_content, 'должно записаться имя функции'
#
#         for item in (4.3, 2.2, 6.5):
#             assert str(item) in log_file_content, f'{item} должен быть записан в файл'


# if __name__ == '__main__':
#     test_2()


@logger('main.log')
def flat_generator(list_of_lists):
    for item in list_of_lists:
        for it in item:
            yield it


if __name__ == '__main__':
    list_of_lists = [[0, 1], [2, 3]]
    flat_generator(list_of_lists)
