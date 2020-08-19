# Evgeny Baranov
# Homework 16 (atm)


class ATM:
    # work bank
    min_limit = 0
    max_limit = 0
    bank_name = 'Mono'

    def __init__(self, amount):
        self.__initial_amount = self._validate_amount(amount)
        self.__currency = 'UAH'
        self.__curr_map = {'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError
        return amount

    def _user_greeting(self): # noqa
        return [f'Вас приветствует банк "{ATM.bank_name}"',
                f'Мы выплачиваем деньги в валюте {self.__currency}', # noqa
                f'Текущий курс USD: {self.__curr_map["USD"]}',
                f'Текущий курс EUR: {self.__curr_map["EUR"]}',
                f'Текущие лимиты на снятие денег: Мин = {self.min_limit}; Макс = {self.max_limit}', # noqa
                'Доступные операции:', 'Вывод денег - [w]',
                'Пополнить счёт - [a]', 'Кол-во денег в банкомате - [c]',
                'Завершить работу - [q]'] # noqa

    def _selection_currency(self):
        print('Вы берете валюту USD - [u], EUR - [e]')
        while True:
            answer = input('Укажите валюту >')
            if answer == 'u':
                return 'USD'
            elif answer == 'e':
                return 'EUR'
            else:
                print('Нет такой валюты')
                continue

    def _user_scars(self):
        while True:
            try:
                custom_sum = int(input('Укажите сумму> '))
                return custom_sum
            except ValueError:
                print('Допустимы только целые числа')
                continue

    def add_money(self, value):
        self.__initial_amount += value
        print(f'Банкомат пополнен на сумму: {value} {self.__currency}')

    def withdraw(self, amount): # noqa
        while True:
            if self.__initial_amount < amount:
                print('Недостаточно денег')
                break
            elif amount > self.max_limit:
                print(f'Превышен максимальный лимит. '
                    f'Максимальный лимит {self.max_limit}') # noqa
                break
            elif amount < self.min_limit:
                print(f'Превышен минимальный лимит. '
                    f'Минимальный лимит {self.min_limit}')  # noqa
                break
            self.__initial_amount -= amount
            print(f'Вы сняли сумму: {amount} {self.__currency}')
            return amount

    @property
    def show_money_amt(self): # noqa
        return f'Количество денег в банкомате {self.__initial_amount} {self.__currency}' # noqa

    # work client
    def user_menu(self):
        work_status = True
        for current_value in self._user_greeting():
            print(current_value)
        while work_status:
            answer = input('Ввод операции> ')
            while True:
                if answer == 'q':
                    work_status = False
                    print(f'Банк {self.bank_name} желает Вам удачи!')
                    print('Отключение.')
                    break
                if answer == 'c':
                    print(self.show_money_amt)
                    break
                elif answer == 'w':
                    current_currency = self.__currency
                    print('Вывод денег:')
                    while True:
                        answer = input('Хотите вывести деньги эквивалентно иностранной валюте? [y/n] >') # noqa
                        if answer == 'n':
                            break
                        elif answer == 'y':
                            current_currency = self._selection_currency() # noqa
                            break
                        else:
                            continue
                    custom_sum = self._user_scars()
                    if current_currency == 'USD':
                        self.withdraw(custom_sum * self.__curr_map['USD']) # noqa
                    elif current_currency == 'EUR':
                        self.withdraw(custom_sum * self.__curr_map['EUR'])
                    else:
                        self.withdraw(custom_sum)
                    break
                elif answer == 'a':
                    while True:
                        current_currency = self.__currency
                        print('Пополнить счёт:')
                        answer = input('Хотите пополнить счет эквивалентно иностранной валюте? [y/n] >') # noqa
                        if answer == 'n':
                            break
                        elif answer == 'y':
                            current_currency = self._selection_currency() # noqa
                            break
                        else:
                            continue
                    custom_sum = self._user_scars()
                    if current_currency == 'USD':
                        self.add_money(custom_sum * self.__curr_map['USD'])
                    elif current_currency == 'EUR':
                        self.add_money(custom_sum * self.__curr_map['EUR'])
                    else:
                        self.add_money(custom_sum)
                    break
                else:
                    print('Нет такой команды')
                    break


if __name__ == '__main__':
    # init atm
    bank_atm = ATM(20000)
    bank_atm.max_limit = 19000
    bank_atm.min_limit = 10
    # client
    bank_atm.user_menu()
