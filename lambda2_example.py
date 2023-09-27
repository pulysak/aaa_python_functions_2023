# Анонимные функции
# В буквальном смысле анонимная функция — это функция без имени.
# В Python анонимная функция создается с помощью ключевого слова лямбда.
# В более широком смысле, ему может быть присвоено или не присвоено имя.

# Тело лямбды - это одно выражение, которое будет возвращено из функции
# Может принимать аргументы

def get_int_id(str_id: str) -> int:
    return int(str_id[2:])


if __name__ == '__main__':
    ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
    print(sorted(ids))  # Lexicographic sort

    sorted_ids = sorted(ids, key=get_int_id)  # Integer sort
    print(sorted_ids)

    # sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Integer sort
    # print(sorted_ids)
