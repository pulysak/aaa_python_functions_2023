# Глобальная переменная.
# Определена на уровне модуля (вне каких-либо функций)
x = 100


def f1():
    # x доступна из любого места программы
    print(x + 1)


def f2():
    # x доступна из любого места программы
    print(x + 1)









def f3():
    # Меняем значение глобальной переменной x
    global x
    x = 200








if __name__ == '__main__':
    f1()

    f3()

    f2()

    print(x)
