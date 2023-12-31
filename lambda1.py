# Анонимные функции
# В буквальном смысле анонимная функция — это функция без имени.
# В Python анонимная функция создается с помощью ключевого слова лямбда.
# В более широком смысле, ему может быть присвоено или не присвоено имя.

# Тело лямбды - это одно выражение, которое будет возвращено из функции
# Может принимать аргументы

def get_int_id(str_id: str) -> int:
    return int(str_id[2:])


get_int_id_lambda = lambda str_id: int(str_id[2:])

print(get_int_id('id100'))
print(get_int_id_lambda('id101'))