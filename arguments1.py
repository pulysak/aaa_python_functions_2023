def hello_world(name: str, age: int, border: str = '!'):
    return f'{border}Hello, world. My name is {name}, my age is {age}{border}'


# Передаем позиционные аргументы
hello_world('Pavel', 29, '!!!')
hello_world(29, 'Pavel', '!!!')

# Передаем именнованные аргументы
hello_world(age=29, name='Pavel', border='!!!')

# Комбинация
hello_world('Pavel', age=29, border='?')

# Опускаем дефолтный(опциональный аргумент)
hello_world('Pavel', age=29)
hello_world('Pavel', 29)