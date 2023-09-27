def fizz_buzz_test(n: int):
    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuzz')
        return
    elif n % 3 == 0:
        print('fizz')
        return
    elif n % 5 == 0:
        print('buzz')
        return
    print(n)


def custom_fizz_buzz(s=None, start=None, end=None):
    items_to_iterate = range(start or 0, (end or 0) + 1)
    if s is not None:
        items_to_iterate = s
        if start is not None or end is not None:
            raise Exception

    for i in items_to_iterate:
        fizz_buzz_test(i)


custom_fizz_buzz(start=1, end=15)
