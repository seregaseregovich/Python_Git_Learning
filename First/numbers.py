def summ(x, y):
    return x + y


def minus(x, y):
    return x - y


def multi(x, y):
    return x * y


def division(x, y):
    return round(x / y, 2)


def main():
    a, b = (input('Enter 2 integer numbers, '
                  'separated by space button, '
                  'please: ')).split(' ')
    print(summ(int(a), int(b)))
    print(minus(int(a), int(b)))
    print(multi(int(a), int(b)))
    print(division(int(a), int(b)))


if __name__ == '__main__':
    print(f'Запуск программы {__name__}')
    main()
else:
    print(f'Запуск импортированного модуля {__name__}.py')
    print('Модуль содержит:'
          ' \n- функцию summ (сложение),'
          ' \n- функцию minus (вычитание),'
          ' \n- функцию multi (умножение),'
          ' \n- функцию division (деление '
          'с округлением до 2х знаков после запятой) ')
