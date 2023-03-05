def summ(x, y):
    return x + y


def minus(x, y):
    return x - y


def multi(x, y):
    return x * y


def division(x, y):
    return x / y


if __name__ == '__main__':
    print(f'Запуск программы {__name__}')
    print(summ(15, 5))
    print(minus(15, 5))
    print(multi(15, 5))
    print(int(division(15, 5)))
else:
    print(f'Запуск импортированного модуля {__name__}.py')
