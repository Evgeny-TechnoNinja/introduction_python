# Evgeny Baranov
# Homework 8

import random
import json
from datetime import datetime


# ******************* task 3 and task 4
def random_number(num_start, num_end):
    return random.randint(num_start, num_end)


def create_date():
    date = datetime.now()
    special_formatted = f'{date.day}-{date.month}-{date.year} ' \
                        f'{date.hour}:{date.minute}:{date.second}'  # noqa
    return special_formatted


def get_number_user(start_num, end_num):
    while True:
        user_custom_num = input(f'Введите число от {start_num} до {end_num}:>')
        try:
            user_custom_num = int(user_custom_num)
        except ValueError:
            print('Нужно указать целое число!')
        if isinstance(user_custom_num, int):
            return user_custom_num


def set_data_json(json_file, obj_result):
    with open(json_file, mode='a') as f:
        json.dump(obj_result, f, indent=4)


def notification(start_num, end_num, attempt):
    print('Игра "Угадай число"')
    print(f'Правила игры очень просты. Ваш компьютер уже загадал число от {start_num} до {end_num}')  # noqa
    print('Вам нужно угадать секретное число. Помните, количество попыток ограничено')  # noqa
    print(f'У вас сейчас есть {attempt} попыток')
    print('Игра началась, удачи!')


STATUS_WINNER = False
JSON_FILE = 'result.json'
START_NUM = 1
END_NUM = 50
SECRET_NUM = random_number(START_NUM, END_NUM)
ATTEMPT = 5
RESULT_DICT = {
    'secret_number': SECRET_NUM,
    'attempt_number': ATTEMPT,
    'date': create_date()
}


def update_data_result():
    RESULT_DICT['secret_number'] = SECRET_NUM
    RESULT_DICT['attempt_number'] = ATTEMPT
    RESULT_DICT['date'] = create_date()


# Show secret num :)
# print(SECRET_NUM)


def game_loop():
    global START_NUM, END_NUM, ATTEMPT, RESULT_DICT, SECRET_NUM, STATUS_WINNER
    while ATTEMPT > 0:
        num = get_number_user(START_NUM, END_NUM)
        if num > 50 or num < 1:
            print(f'Вы вышли за диапазон ({START_NUM}-{END_NUM}) и потратили попытку впустую') # noqa
        ATTEMPT -= 1
        update_data_result()
        if num < SECRET_NUM:
            print('Секретное число больше чем это')
            print(f'Попыток: {ATTEMPT}')
        elif num > SECRET_NUM:
            print('Секретное число меньше чем это')
            print(f'Попыток: {ATTEMPT}')
        else:
            print('Поздравляю! Вы угадали секретное число!')
            STATUS_WINNER = True
            break
    if STATUS_WINNER is False:
        print('Вы проиграли!')


def main():
    global START_NUM, END_NUM, ATTEMPT, STATUS_WINNER, JSON_FILE, RESULT_DICT
    notification(START_NUM, END_NUM, ATTEMPT)
    game_loop()
    if STATUS_WINNER:
        set_data_json(JSON_FILE, RESULT_DICT)


if __name__ == '__main__':
    main()
