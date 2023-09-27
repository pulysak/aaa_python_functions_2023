def f1():
    print('f1')


def f2():
    print('f2')


def f3():
    print('f3')


def function_getter():
    def f():
        print('I am function from functon getter')

    return f


def function_runner(f):
    f()


if __name__ == '__main__':
    print('Functions in list')
    for f in [f1, f2, f3]:
        f()

    print('-' * 100)

    print('Functions in dict')
    d = {
        1: f1,
        2: f2,
        3: f3,
    }
    d[1]()

    print('-' * 100)

    func = function_getter()
    func()
    function_runner(func)
