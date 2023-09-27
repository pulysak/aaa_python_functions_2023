# Хотим добавить к набору функций, новый одинаковый функционал.
# Например хотим выводить сообщение в конце и в начале каждой функции
from typing import Callable


def before_after_decorator(f: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('Before function')
        result = f(*args, **kwargs)
        print('After function')
        return result

    return wrapper


@before_after_decorator
def f1():
    return 1


@before_after_decorator
def f2():
    return 2


@before_after_decorator
def f3():
    return 3


@before_after_decorator
def f4():
    return 4


@before_after_decorator
def f5():
    return 5


if __name__ == '__main__':
    print(f1(), '-' * 100)
    print(f2(), '-' * 100)
    print(f3(), '-' * 100)
    print(f4(), '-' * 100)
    print(f5(), '-' * 100)
