# Evgeny Baranov
# Homework 9

# ******************* task (review)
# Описание ревью начинается с 30 строки!
import random

y_n = 'yes'
while y_n == 'yes':
    random_number = random.randint(1, 1000)
    for i in range(10):
        print(f'У вас {10 - i} попыток!')
        try: # noqa
            player_select = int(input('Введите число:'))
        except ValueError as err:
            print(err)
            print('Error you number not correct!')
            y_n = 'error'
            break
        if player_select == random_number:
            print('You win!!!!')
            y_n = input('Хотите прожолжить?[yes/no]')
            break
        elif player_select > random_number:
            print('Вваше число больше')
        elif player_select < random_number:
            print('Вваше число Меньше')

# Первый взгляд

# Первое, что бросилось в глаза - это имя переменной "y_n",
# что не очень информативно. Я думаю имена
# переменных должны быть такими, чтобы код был самодокументированным.
# Также из контекста кода
# видно, что переменной "y_n" присваивается строка "error",
# что также не очень хорошо, поскольку видно, что
# в переменной ожидается "yes" или "no". Лучше заменить на булево значение.


# Также в конструкции исключений используется
# псевдоним для ошибки "err", поскольку
# это ошибка явно никак не отображается и как-то еще не используется,
# этот псевдоним ни к чему. Потому что
# просто показывается кастомный текст во время ошибки.

# Можно по-другому переписать условные операторы,
# на мой взгляд более семантически представить их, как-то так:
# "если - ещё если - ещё"


# Первый запуск кода

# Конечно, цикл рабочий. Но назвать программу "юзер френдли" нельзя,
# потому что если игра закончилась, то сразу
# начинается не спрашивая, хочет пользователь играть или нет.
# Также нет никакого уведомления о выходе за диапазон.
# Также программа вылетает, если пользователь вводит строку,
# или просто нажмёт "enter", то есть прекратит работу,
# выводя "Error you number not correct!".
# Из вышеописанного следует, что бизнес логика организована на скорую руку.


# Что происходит под капотом

# import random Происходит импорт модуля
# y_n = 'yes' Инициализируется переменная в глобальной области видимости, котрой присвоена строка  # noqa
# while y_n == 'yes': Создаётся цикл, который работает, пока переменная y_n == 'yes', что дает True  # noqa
# random_number = random.randint(1, 1000) Переменной присваивается случайное число, результатом работы  # noqa
# функции randint.
# for i in range(10) Инициализируется цикл, который будет выполнен 10 раз, количество раз генерирует  # noqa
# функция range() - делает список, который состоит из прогрессии.
# print(f'У вас {10 - i} попыток!') выводится количество попыток
#         try:
#            player_select = int(input('Введите число:')) #  запрашивается у пользователя число # noqa
#        except ValueError as err:
#            print('Error you number not correct!') # Уведомление в случае ошибки  # noqa
#            y_n = 'error' # Присвоение значения в переменной
#            break # Прерывание цикла
# Выше строится "конструкция" для обработки ошибок.
#        if player_select == random_number: # проверка равняется число пользователя рандомному числу  # noqa
#            print('You win!!!!') # Уведомление о победе
#            y_n = input('Хотите продолжить?[yes/no]') # Работа функции инпут, результат присваивается в перем.  # noqa
#            break # Прерывание цикла
#        elif player_select > random_number: # Проверка пользовательского числа на больше  # noqa
#            print('Ваше число больше') # Уведомления, работа функции print
#        elif player_select < random_number: # Проверка пользовательского числа на меньше  # noqa
#            print('Ваше число Меньше') # Работает функция print
# Выше идут операторы ветвления

# Вкратце работа такая, 10 раз будет запрошено число, и 10 раз пройдет проверка в ветке, от числа  # noqa
# пользователя зависит в какую ветку зайдет программа и что будет дальше.

# Также есть опечатки в словах, но на роботе программы это отображается.

# Смотрите файл new_code.py - там будет переписана программа, переорганизован код. # noqa
