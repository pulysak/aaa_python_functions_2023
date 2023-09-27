def hello_world(name: str, age: int) -> str | None:
    if age <= 0:
        return

    return f'Hello, world. My name is {name}'


greeting = hello_world('Name', 'twenty nine')

if greeting > 5:
    print('What?!')
