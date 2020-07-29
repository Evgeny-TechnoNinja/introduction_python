# Evgeny Baranov
# Homework 11

from random import sample

# ******************* task (game slot machine)

# ========== data
slot_setting = {
    'reels': {
        'wheel': ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"],
    },
    'item_weight': {
     'XXX': 5,
     'A': 4.5,
     'B': 4,
     'C': 3.5,
     'D': 3,
     'E': 2.5,
     'F': 2,
     'G': 1.5,
     'H': 1,
     'I': 0.5
    },
    'minimum_rate': 10
}

SLOT_STATUS = {'run': True}

PLAYER = {
    'credit': 500,
    'win': 0,
    'paid': 0,
    'uploaded_card': False
}

STATISTICS_GAME = {
    'player_credit': 0,
    'player_wins': 0,
    'casino_paid': [],

}
# ================


# ======== service
def shuffle_wheel(dict_slot_setting, dict_setting_name, key_setting, num_passes, take_items): # noqa
    result = []
    for current_value in range(num_passes):
        result.append(sample(dict_slot_setting[dict_setting_name][key_setting], take_items)) # noqa
    return result


def get_result_combination(obj_combs, dict_slot_setting, dict_setting_name, name_joker): # noqa
    item_counter = 1
    selection_counter = 0
    temp_result = 0
    i = 0
    while i < len(obj_combs):
        if obj_combs[i] == obj_combs[item_counter]:
            elem_value = dict_slot_setting[dict_setting_name].get(obj_combs[i][0]) # noqa
            selection_counter += 1
            if selection_counter == 1 and obj_combs.count([name_joker]) == 0:
                temp_result = elem_value + elem_value
            elif selection_counter == 1 and obj_combs.count([name_joker]) == 1:
                temp_result = elem_value + elem_value
                temp_result = temp_result * 2
            elif selection_counter == 1 and obj_combs[1] == [name_joker]\
                    and obj_combs.count([name_joker]) == 2:
                temp_result = elem_value + elem_value
            elif selection_counter == 2 or selection_counter == 2\
                    and obj_combs.count([name_joker]) == 3:
                temp_result = elem_value + elem_value
                temp_result = temp_result * 10
        item_counter += 1
        if item_counter == len(obj_combs):
            break
        i += 1
    return temp_result


def subtract_credit(dict_player, key_credit, dict_slot_setting, key_rate):
    dict_player[key_credit] -= dict_slot_setting[key_rate]


def update_card_status(dict_player, key_status_card, status_bool):
    dict_player[key_status_card] = status_bool


def update_credit(dict_player, key_credit, paid_sum):
    dict_player[key_credit] = dict_player[paid_sum]
    dict_player[paid_sum] = 0


def update_current_winn(dict_player, key_win, current_result, key_paid):
    dict_player[key_win] = int(current_result)
    if dict_player[key_win] > 0:
        dict_player[key_paid] += int(current_result)


def show_combination_reels(result_mix):
    print(result_mix)


def show_game_state(dict_player, key_credit, key_win, key_paid):
    print(f'Game state: | Credit: {dict_player[key_credit]}' # noqa
          f' | Win: {dict_player[key_win]}'
          f' | Paid: {dict_player[key_paid]}')


def show_statistics(dict_statistics, key_player_credit, key_player_wins, key_casino_paid): # noqa
    print('Game statistics')
    print(f'Maximum credit: {dict_statistics[key_player_credit]}')
    print(f'Total wins: {dict_statistics[key_player_wins]}')
    print(f'Casino paid {sum(dict_statistics[key_casino_paid])}')


def show_symbol_table():
    print('       Symbol payout table         ')
    print('ITEMS       3       2       2 + XXX')
    print('------------------------------------')
    print('XXX         100     10      100')
    print('A           90      9       18')
    print('B           80      8       16')
    print('C           70      7       14')
    print('D           60      6       12')
    print('E           50      5       10')
    print('F           40      4       8')
    print('G           30      3       6')
    print('H           20      2       4')
    print('I           10      1       2')


def informing():
    print('Welcome to casino "Two pockets"')
    print('The rules of the game are very simple, play while you have credit')


def info_credit(dict_player, key_credit, dict_slot_setting, key_rate):
    print(f'Your credit: {dict_player[key_credit]}')
    print(f'Credit is taken away for a spin: {dict_slot_setting[key_rate]}')


def add_statistics_credit(dict_statistics, key_player_credit, dict_player, key_credit): # noqa
    dict_statistics[key_player_credit] += dict_player[key_credit]


def counter_statistics_win(dict_statistics, key_player_win):
    dict_statistics[key_player_win] += 1


def add_statistics_payout(dict_statistics, key_player_paid,  dict_player, key_paid): # noqa
    dict_statistics[key_player_paid].append(dict_player[key_paid])
# ================


# ===== main mechanism
def game_loop():
    global PLAYER, SLOT_STATUS, STATISTICS_GAME
    while SLOT_STATUS['run']:
        info_credit(PLAYER, 'credit', slot_setting, 'minimum_rate')
        if PLAYER['uploaded_card']:
            if PLAYER['credit'] < slot_setting['minimum_rate']:
                print('No funds to continue playing!')
                SLOT_STATUS['run'] = False
                break
            else:
                PLAYER['uploaded_card'] = False
        while True:
            answer = input('Do you want to play? [y/n]>')
            if answer == 'y':
                add_statistics_credit(STATISTICS_GAME, 'player_credit', PLAYER, 'credit') # noqa
                break
            elif answer == 'n':
                break
        if answer == 'y':
            while PLAYER['credit'] > 0:
                answer = input('Spin slots, play? [y/n]>')
                if answer == 'y':
                    subtract_credit(PLAYER, 'credit', slot_setting, 'minimum_rate') # noqa
                    random_combinations = shuffle_wheel(slot_setting, 'reels', 'wheel', 3, 1) # noqa
                    show_combination_reels(random_combinations)
                    num_result_combinations = get_result_combination(
                        random_combinations, slot_setting, 'item_weight', 'XXX'
                    )
                    update_current_winn(PLAYER, 'win', num_result_combinations, 'paid') # noqa
                    show_game_state(PLAYER, 'credit', 'win', 'paid')
                    if PLAYER['win'] > 0:
                        counter_statistics_win(STATISTICS_GAME, 'player_wins')
                    if PLAYER['credit'] == 0:
                        add_statistics_payout(STATISTICS_GAME, 'casino_paid', PLAYER, 'paid') # noqa
                        print('You are out of credit')
                        answer = input('Top up card with is credit? [y/n]')
                        if answer == 'y':
                            if PLAYER['paid'] > 0:
                                update_credit(PLAYER, 'credit', 'paid')
                                update_card_status(PLAYER, 'uploaded_card', True) # noqa
                                break
                            else:
                                print('No funds to top up your card, you are bankrupt!') # noqa
                                SLOT_STATUS['run'] = False
                        elif answer == 'n':
                            print('Goodbye')
                            SLOT_STATUS['run'] = False
                elif answer == 'n':
                    add_statistics_payout(STATISTICS_GAME, 'casino_paid', PLAYER, 'paid') # noqa
                    print('Goodbye')
                    SLOT_STATUS['run'] = False
                    break
            else:
                add_statistics_payout(STATISTICS_GAME, 'casino_paid', PLAYER, 'paid') # noqa
                print('You are bankrupt!')
                SLOT_STATUS['run'] = False
        elif answer == 'n':
            print('Goodbye')
            SLOT_STATUS['run'] = False


def main():
    informing()
    show_symbol_table()
    game_loop()
    show_statistics(STATISTICS_GAME, 'player_credit', 'player_wins', 'casino_paid') # noqa


if __name__ == '__main__':
    main()
