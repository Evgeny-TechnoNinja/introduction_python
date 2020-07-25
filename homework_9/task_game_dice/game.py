# Evgeny Baranov
# Homework 9

from random import randint
from datetime import datetime
import json


# ******************* task (game dice)
def random_number_create(num_start, num_end):
    return randint(num_start, num_end)


def create_date():
    date = datetime.now()
    special_formatted = f'{date.day}-{date.month}-{date.year} ' \
                        f'{date.hour}:{date.minute}:{date.second}'  # noqa
    return special_formatted


def set_data_json(json_file, obj_result):
    with open(json_file, mode='a') as f:
        json.dump(obj_result, f, indent=4)


def username_create(dict_setting, key_setting_min, key_setting_max):
    while True:
        user = input('Укажите ваше имя:>')
        if user.isspace():
            print('Имя из одних пробелов не подходит!')
        elif user.isdigit():
            print('Имя из одних чисел не подходит')
        else:
            user = user.strip()
            if len(user) < dict_setting[key_setting_min]:
                print('Слишком короткое имя!')
            elif len(user) > dict_setting[key_setting_max]:
                print('Слишком длинное имя!')
            else:
                return user


PLAYER_ONE = {
    'name': None,
    'run': False,
    'points': []
}

PLAYER_TWO = {
    'name': None,
    'run': False,
    'points': []
}

PLAY_SETTING = {
    'status_run': True,
    'number_throws': 10,
    'cubes_quantity': 2
}

REC_WINNER = {
    'name': None,
    'points': None,
    'date': ''
}

JSON_WINN = 'winner.json'

name_setting = {
    'letter_min': 3,
    'letter_max': 6
}

dice = {
    'value_min': 1,
    'value_max': 6
}


def game_inform():
    print('Простая игра в "Кости", игроки бросают кости по очереди')
    print('Кто набрал большую сумму, тот и победил.\n')


def info_registration(dict_setting, key_setting_min, key_setting_max):
    print(f'Имя не должно быть короче {dict_setting[key_setting_min]}'
          f' и больше {dict_setting[key_setting_max]}')  # noqa
    print('Имя не сможет состоять из одних пробелов и цифр\n')


def player_registration(player_one, player_two): # noqa
    info_registration(name_setting, 'letter_min', 'letter_max')
    print('Регистрация первого игрока')
    player_one['name'] = username_create(name_setting, 'letter_min', 'letter_max')  # noqa
    print('Регистрация второго игрока')
    player_two['name'] = username_create(name_setting, 'letter_min', 'letter_max')  # noqa
    return True


def dice_rolls(dict_dice, key_min, key_max, dict_play_setting, key_cubes_quantity): # noqa
    result = []
    for i in range(dict_play_setting[key_cubes_quantity]):
        random_num = random_number_create(dict_dice[key_min], dict_dice[key_max]) # noqa
        result.append(random_num)
    return result


def show_moves(txt, dict_play_setting, key_throws):
    print(f'{txt}: {dict_play_setting[key_throws]}')


def show_throw(dict_player, key_name, dict_play_setting, key_cubes_quantity, result): # noqa
    show_result = [[current_value] for current_value in result]
    print(f'Игроку {dict_player[key_name]}, '
          f'на {dict_play_setting[key_cubes_quantity]} '
          f'кубиках выпало: {show_result}\n')


def show_winner(dict_player_one, key_name_one, dict_player_two, key_name_two, sum_one, sum_two): # noqa
    if sum_one == sum_two:
        print(f'У нас два победителя - это {dict_player_one[key_name_one]}'
              f' и {dict_player_two[key_name_two]}!'.upper())
        print(f'{dict_player_one[key_name_one]} набрал сумму: {sum_one}')
        print(f'{dict_player_two[key_name_two]} набрал сумму: {sum_two}')
    elif sum_one > sum_two:
        print(f'{dict_player_one[key_name_one]} набрал сумму: {sum_one}')
        print(f'{dict_player_two[key_name_two]} набрал сумму: {sum_two}') # noqa
        print(f'{dict_player_two[key_name_two]} проиграл')
        print(f'Победил {dict_player_one[key_name_one]}!!!'.upper())
    elif sum_one < sum_two:
        print(f'{dict_player_two[key_name_two]} набрал сумму: {sum_two}')
        print(f'{dict_player_one[key_name_one]} набрал сумму: {sum_one}') # noqa
        print(f'{dict_player_one[key_name_one]} проиграл')
        print(f'Победил {dict_player_two[key_name_two]}!!!'.upper())


def take_winner(dict_player_one, key_point_one, dict_player_two, key_point_two): # noqa
    winners = []
    if sum(dict_player_one[key_point_one]) == sum(dict_player_two[key_point_two]):
        winners.append(dict_player_one)
        winners.append(dict_player_two)
        return winners
    elif sum(dict_player_one[key_point_one]) > sum(dict_player_two[key_point_two]):
        winners.append(dict_player_one)
        return winners
    elif sum(dict_player_one[key_point_one]) < sum(dict_player_two[key_point_two]):
        winners.append(dict_player_two)
        return winners


def rec_data(list_winn, rec_win, key_name_name, key_name_point,
             rec_json_func, json_file, key_name_date, create_date): # noqa
    for current_value in list_winn:
        for key_value in current_value.items():
            if key_value[0] == key_name_name:
                rec_win[key_name_name] = key_value[1]
            elif key_value[0] == key_name_point:
                rec_win[key_name_point] = sum(key_value[1])
        rec_win[key_name_date] = create_date()
        rec_json_func(json_file, rec_win)


def add_points(dict_play_setting, key_point, result):
    dict_play_setting[key_point].append(sum(result))


def del_points(dict_player, key_point):
    dict_player[key_point].pop()


def total_points(dict_player, key_point):
    return sum(dict_player[key_point])


def game_loop():
    global PLAY_SETTING, PLAYER_ONE, PLAYER_TWO
    while PLAY_SETTING['status_run']:
        while True:
            show_moves('Осталось всего бросков', PLAY_SETTING, 'number_throws')
            answer = input(f'Игрок {PLAYER_ONE["name"]} готов бросить кубики? [y/n]>') # noqa
            if answer == 'y' or answer == 'n':
                break
        if answer == 'y':
            PLAYER_ONE['run'] = True
            while PLAYER_ONE['run']:
                throw = dice_rolls(dice, 'value_min', 'value_max', PLAY_SETTING, 'cubes_quantity') # noqa
                show_throw(PLAYER_ONE, 'name', PLAY_SETTING, 'cubes_quantity', throw) # noqa
                add_points(PLAYER_ONE, 'points', throw)
                PLAYER_ONE['run'] = False
        elif answer == 'n':
            print(f'Игрок {PLAYER_ONE["name"]} прерывает игру')
            print(f'Игрок {PLAYER_ONE["name"]} проиграл')
            PLAY_SETTING['status_run'] = False
            break
        while True:
            show_moves('Осталось всего бросков', PLAY_SETTING, 'number_throws')
            answer = input(f'Игрок {PLAYER_TWO["name"]} готов бросить кубики? [y/n]>')  # noqa
            if answer == 'y' or answer == 'n':
                break
        if answer == 'y':
            PLAYER_TWO['run'] = True
            while PLAYER_TWO['run']:
                throw = dice_rolls(dice, 'value_min', 'value_max', PLAY_SETTING, 'cubes_quantity')  # noqa
                show_throw(PLAYER_TWO, 'name', PLAY_SETTING, 'cubes_quantity', throw) # noqa
                add_points(PLAYER_TWO, 'points', throw)
                PLAYER_TWO['run'] = False
        elif answer == 'n':
            print(f'Игрок {PLAYER_TWO["name"]} прерывает игру')
            print(f'Игрок {PLAYER_TWO["name"]} проиграл')
            PLAY_SETTING['status_run'] = False
            break
        if PLAYER_ONE['points'] == PLAYER_TWO['points']:
            del_points(PLAYER_ONE, 'points')
            del_points(PLAYER_TWO, 'points')
        PLAY_SETTING['number_throws'] -= 1
        if PLAY_SETTING['number_throws'] == 0:
            sum_player_one = total_points(PLAYER_ONE, 'points')
            sum_player_two = total_points(PLAYER_TWO, 'points')
            show_winner(PLAYER_ONE, 'name', PLAYER_TWO, 'name', sum_player_one, sum_player_two) # noqa
            winner = take_winner(PLAYER_ONE, 'points', PLAYER_TWO, 'points')
            PLAY_SETTING['status_run'] = False
            return winner


def main():
    global REC_WINNER
    game_inform()
    if player_registration(PLAYER_ONE, PLAYER_TWO): # noqa
        winner = game_loop()
        if len(winner) > 0 and isinstance(winner, list):
            rec_data(winner, REC_WINNER, 'name', 'points',
                     set_data_json, JSON_WINN, 'date', create_date)
        else:
            print('Невозможно записать данные!')
    else:
        print('Регистрация игроков не прошла успешно!'.upper())


if __name__ == '__main__':
    main()
