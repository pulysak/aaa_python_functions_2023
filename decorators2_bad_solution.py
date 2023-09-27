# Хотим добавить к набору функций, новый одинаковый функционал.
# Например хотим выводить сообщение в конце и в начале каждой функции


def f1():
    print('Before function')
    result = 1
    print('After function')
    return result


def f2():
    print('Before function')
    result = 2
    print('After function')
    return result


def f3():
    return 3


def f4():
    return 4


def f5():
    return 5


if __name__ == '__main__':
    print(f1(), '-' * 100)
    print(f2(), '-' * 100)
    print(f3(), '-' * 100)
    print(f4(), '-' * 100)
    print(f5(), '-' * 100)
