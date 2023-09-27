# Что будет лежать в args?

def hello_world(name: str, age: int, border: str = '!', *args, **kwargs) -> str:
    print(args)
    print(kwargs)
    return f'{border}Hello, world. My name is {name}, my age is {age}{border}'


hello_world('John', 55, '!', 'x', 'y', 'z', foo='some_param', bar=1, baz=[1, 3, 3])


def accept_anything(*args, **kwargs):
    print(args, kwargs)


accept_anything(1, 2, 'a', a=2, foo=10500)
accept_anything()
accept_anything(1, 2, 3, 4, 5)
accept_anything(a=1, b=2, c=3)
