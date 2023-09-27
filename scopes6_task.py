# Нужно написать функцию, которая будет работаь следующим образом.

# custom_sum(2) -> 2
# custom_sum(3) -> 5
# custom_sum(5) -> 10
# custom_sum(1) -> 11
# custom_sum(-10) -> 1















def custom_sum_getter():
    s = 0

    def custom_sum(x: int) -> int:
        nonlocal s
        s += x
        return s

    return custom_sum




if __name__ == '__main__':
    custom_sum = custom_sum_getter()
    print(custom_sum(2))
    print(custom_sum(3))
    print(custom_sum(5))
    print(custom_sum(1))
    print(custom_sum(-10))
