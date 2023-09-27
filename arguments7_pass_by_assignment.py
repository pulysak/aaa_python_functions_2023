x = 1


def add_to_int(param: int):
    param = param + 1
    print(param)


l1 = [1]


def add_to_list(param: list):
    param.append(2)
    print(param)


if __name__ == '__main__':
    print('Before add to int')
    add_to_int(x)
    print('After add to int')
    print(x)

    # print('-'*100)
    #
    # print('Before add to list')
    # add_to_list(l1)
    # print('After add to list')
    # print(l1)

