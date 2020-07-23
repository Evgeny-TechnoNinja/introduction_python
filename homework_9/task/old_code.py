import random

y_n = 'yes'
while y_n == 'yes':
    random_number = random.randint(1, 1000)
    for i in range(10):
        print(f'У вас {10 - i} попыток!')
        try:
            player_select = int(input('Введите число:'))
        except ValueError as err:
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