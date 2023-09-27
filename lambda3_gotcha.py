# Анонимные функции

def list_lambda_factory():
    lambda_list = []
    for i in range(3):
        lambda_list.append(lambda: i)

    return lambda_list


if __name__ == '__main__':
    lambda_list = list_lambda_factory()

    for f in lambda_list:
        print(f())
