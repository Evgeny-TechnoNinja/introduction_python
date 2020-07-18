from Intro import intro
from Help import calc_help
from Add import add
from Divide import divide
from Subtract import subtract
from Multiply import multiply


def main():
    intro.intro()
    while True:
        status = input('Хотите получить справку о программе [y/n]> ')
        if status == 'y':
            calc_help.calc_help()
            break
        elif status == 'n':
            break
    while True:
        status = input('Приступить к вычислениям [y/n]> ')
        if status == 'y':
            print('Процесс...')
            while True:
                custom_number_a = input('Введите первое число:>')
                try:
                    custom_number_a = int(custom_number_a)
                except ValueError:
                    print('Работаю только с числами!')
                if isinstance(custom_number_a, int):
                    break
            while True:
                print('["+", "-", "*", "/"]')
                math_operation = input('Введите тип операции:>')
                if math_operation in ['+', '-', '*', '/']:
                    break
                else:
                    print('Непонятный символ')
            while True: # noqa
                custom_number_b = input('Введите второе число:>')
                try:
                    custom_number_b = int(custom_number_b)
                except ValueError:
                    print('Работаю только с числами!')
                if isinstance(custom_number_b, int):
                    break
            if math_operation == '+':
                print(f'{custom_number_a} {math_operation} {custom_number_b}'
                      f' = {add.add(custom_number_a, custom_number_b)}')
            elif math_operation == '-':
                print(f'{custom_number_a} {math_operation} {custom_number_b}'
                      f' = {subtract.subtract(custom_number_a, custom_number_b)}')
            elif math_operation == '*':
                print(f'{custom_number_a} {math_operation} {custom_number_b}'
                      f' = {multiply.multiply(custom_number_a, custom_number_b)}')
            elif math_operation == '/':
                try:
                    print(f'{custom_number_a} {math_operation} {custom_number_b}'
                      f' = {divide.divide(custom_number_a, custom_number_b)}') # noqa
                except ZeroDivisionError:
                    print('Уважаемый Юзер, на 0 делить нельзя!')
        elif status == 'n':
            print('Я выключаюсь, пока, Юзер!')
            break


if __name__ == '__main__':
    main()


