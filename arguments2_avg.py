# В некоторых случаях, когда вы определяете функцию, вы можете заранее не знать, сколько аргументов вы хотите, чтобы она принимала.
# Предположим, например, что вы хотите написать функцию Python, которая вычисляет среднее значение нескольких значений.


def avg(a, b, c):
    return (a + b + c) / 3


print(avg(1, 2, 3))
print(avg(1, 2, 3, 4))
