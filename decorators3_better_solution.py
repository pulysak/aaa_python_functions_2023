# Хотим добавить к набору функций, новый одинаковый функционал.
# Например хотим выводить сообщение в конце и в начале каждой функции
# Какие проблемы есть в этом решении?
from typing import Callable


def before_after_decorator(f: Callable) -> Callable:
    def wrapper():
        print('Before function')
        result = f()
        print('After function')
        return result

    return wrapper


def f1():
    return 1


f1 = before_after_decorator(f1)


def f2():
    return 2


f2 = before_after_decorator(f2)


def f3():
    return 3


f3 = before_after_decorator(f3)


def f4():
    return 4


f4 = before_after_decorator(f4)


def f5():
    return 5


f5 = before_after_decorator(f5)

if __name__ == '__main__':
    print(f1(), '-' * 100)
    print(f2(), '-' * 100)
    print(f3(), '-' * 100)
    print(f4(), '-' * 100)
    print(f5(), '-' * 100)
