def outer():
    outer_x = 'outer_x'

    print('In OUTER function', outer_x)

    def inner():
        # Функция inner имеет доступ к имени outer_x (имя лежит в нелокальной области видимости)
        print('In INNER function', outer_x)

    inner()


def outer2():
    outer_x = 'outer_x'

    def inner():
        outer_x = 'inner_x'
        print('In INNER function', outer_x)

    inner()
    print('In OUTER function', outer_x)


def outer3():
    outer_x = 'outer_x'

    def inner():
        nonlocal outer_x
        outer_x = 'inner_x'
        print('In INNER function', outer_x)

    inner()
    print('In OUTER function', outer_x)


if __name__ == '__main__':
    print('outer')
    outer()
    print('-' * 100)

    print('outer2')
    outer2()
    print('-' * 100)

    print('outer3')
    outer3()
    print('-' * 100)
