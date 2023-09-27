# Есть похожий механизм, чтобы функция могла принять любое количество key-word аргументов. Для этого используется специальный параметр, который обычно называют kwargs перед которым ставят 2 звезды. Тогда все именнованные аргементы, для которых не нашелся соответствующий параметр попадут в кваргс.
# Кваргс имеет тип dict - словарь.


def hello_world(name: str, age: int, border: str = '!', **kwargs) -> str:
    print(kwargs)
    return f'{border}Hello, world. My name is {name}, my age is {age}{border}'

hello_world('John', 55, foo='some_param', bar=1, baz=[1, 3, 3])