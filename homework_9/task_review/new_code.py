# Evgeny Baranov
# Homework 9

# ******************* task (review, New code)
from random import randint


def random_number_create(num_start, num_end):
    return randint(num_start, num_end)


def dialog_create(txt):
    return input(txt)


def get_number_user(inp_txt, err_txt):
    while True:
        player_select = input(f'{inp_txt}:>')# noqa
        try:
            player_select = int(player_select)
            return player_select
        except ValueError:
            print(f'{err_txt}')


GAME_STATUS = True
game_options = {
    'start_num': 1,
    'end_num': 1000,
    'attempts': 10
}


def notification(option):
    print('Игра угадай число')
    print(f'Вам нужно угадать число в диапазоне от '
          f'{option["start_num"]} до {option["end_num"]}')
    print(f'У вас есть всего {option["attempts"]} попыток\n')


def game_process(option, random_num, get_num):
    for i in range(option['attempts']):
        print(f'У вас {option["attempts"] - i} попыток')
        player_select_num = get_num('Введите число', 'Укажите целое число')  # noqa
        if player_select_num < option['start_num'] or player_select_num > option['end_num']: # noqa
            print(f'Не выходите за диапазон '
                  f'({option["start_num"]}-{option["end_num"]}) вы тратите попытки пустую!') # noqa
        if player_select_num > random_num:
            print('Ваше число больше')
        elif player_select_num < random_num:
            print('Ваше число меньше')
        else:
            print('Поздравляю! Вы угадали число!'.upper())
            break
    else:
        print('Вы проиграли!'.upper())


def game_loop(option):
    global GAME_STATUS
    while GAME_STATUS:
        random_num = random_number_create(option['start_num'], option['end_num']) # noqa
        # print(random_num)
        answer = dialog_create('Вы хотите начать игру? [yes/no]>')
        if answer == 'yes':
            game_process(game_options, random_num, get_number_user)
        elif answer == 'no':
            print('Выход из игры')
            GAME_STATUS = False
        else:
            print('Не могу разобрать ваш ответ!')


def main():
    notification(game_options)
    game_loop(game_options)


if __name__ == '__main__':
    main()

