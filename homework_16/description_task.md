# ДЗ №16

## Банкомат
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.

**Что делать дома**:
    - реализовать конвертацию c различных валют в гривну при добавлении денег в банкомат и при снятии


```python
from dataclasses import dataclass


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    min_limit = 0
    max_limit = 0
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.currency = 'UAH'
        self.curr_map = {'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amout):
        if amout < 0:
            raise ValueError
        return amout

    def add_money(self, valoe):
        self.initial_amount += ...

    def withdraw(self, amount):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError(')))))')
        self.initial_amount -= amount
        return amount

```

## KOLOBOK

**Задание:**
Нужно дописать основную линию сказки. Каждого героя реализовать классом с методами. 
Так же должен быть класс сказки (или функция), где происходит основное действие с героями


```python
# ___________KOLOBOK_______________

class Hero:
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    pass


class Babka(Hero):
    def bake_colobok(self):
        return Colobok('Kolobok')


class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.colobok = None

    def babkin_dom(self):
        self.ded.tel_babka_about_colobok()
        self.colobok = self.babka.bake_colobok()

    def start(self):
        self.babkin_dom()


my_tail = Tale('L', ';')

my_tail.start()
```
