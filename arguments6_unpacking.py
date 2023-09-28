# Не путать

def hello_world(name: str, age: int) -> str:
    return f'Hello, world. My name is {name}, my age is {age}'


foo = ['John', 55]
hello_world(foo[0], foo[1])
hello_world(*foo)
hello_world('John', 55)

bar = {
    'name': 'John',
    'age': 55,
}
hello_world(name=bar['name'], age=bar['age'])
hello_world(**bar)
hello_world(name='John', age=55)
