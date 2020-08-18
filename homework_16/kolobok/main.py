# Evgeny Baranov
# Homework 16 (kolobok)

import sys


class Hero:
    def __init__(self, name, cunning=0, alive=True,):
        self.name = name
        self.cunning = cunning
        self.alive = alive

    def speak(self, txt):
        print(txt)


class Enemy(Hero):
    def eat_hero(self, hero_cunning, hero_alive, cunning):
        if hero_cunning < cunning:
            hero_alive = False
        return hero_alive


class GingerBreadMan(Hero):
    """ the main character """
    def __init__(self, name, diameter, weight, material):
        super().__init__(name)
        self.diameter = diameter
        self.weight = weight
        self.material = material

    def roll(self, bool_status):
        status = bool_status
        if status:
            print('Я покатился...')
        else:
            print('Я стою на месте')
        return status

    def sing(self, enemy_name):
        sing_list = ['Я Колобок, Колобок!', 'Я по коробу скребен!',
                     'Я всех хитрей!', f'Я от тебя {enemy_name} уйду!']
        return sing_list # noqa

    @property
    def characteristic(self):
        typical = {
            'diameter': self.diameter,
            'weight': self.weight,
            'material': self.material
        }
        return typical


class Stock:
    """ barn where products """
    def __init__(self, material, quantity):
        self.__material = material
        self.__quantity = quantity

    def __vault(self):
        vault = {
            'material_name': self.__material,
            'material_quantity': self.__quantity
        }
        return vault

    @property
    def get_material_name(self):
        resource = self.__vault()
        return resource['material_name']

    def hand_out(self, quantity_num):
        resource = self.__vault()
        if resource['material_quantity'] >= quantity_num:
            resource['material_quantity'] -= quantity_num
            return quantity_num
        print('Нет такого количества материала!')
        return 0


class Grandad(Hero):
    """ GingerBreadMan engineer"""
    def project_hero_tale(self, diameter, weight, material_quantity, material='flour'): # noqa
        parameters = {
            'diameter': diameter,
            'weight': weight,
            'material_quantity': material_quantity,
            'material': material,
        }
        return parameters


class Gran(Hero):
    """ GingerBreadMan creator """
    def take_away_stock(self, parameter, field_material_name,
                        field_diameter_name, field_weight_name,
                        get_material_name, material_hand_out): # noqa
        basket = {}
        if parameter[field_material_name] == get_material_name:
            basket['diameter'] = parameter[field_diameter_name]
            basket['weight'] = parameter[field_weight_name]
            basket['material'] = get_material_name
            basket['material_quantity'] = material_hand_out
            if basket['material_quantity'] > 0:
                return basket
        return False

    def create_hero_tale(self, class_name, name, basket):
        temp_list = [name]
        for items in basket.items():
            if items[0] != 'material_quantity':
                temp_list.append(items[1])
        result_hero = class_name(*temp_list)
        basket.clear()
        return result_hero


class Tale:
    def __init__(self, barn, grandad, gran, enemy):
        self.barn = barn
        self.grandad = grandad
        self.gran = gran
        self.enemy = enemy

    def scene_grandad_home(self, grandad, gran, barn):
        print(f'Просит дед {grandad.name}, бабку {gran.name}, испечь Колобка')
        parameter_hero = grandad.project_hero_tale(80, 20, 100, 'flour') # noqa
        basket = gran.take_away_stock(parameter_hero, 'material', 'diameter', 'weight', # noqa
                                      barn.get_material_name, barn.hand_out(100)) # noqa

        def create_main_hero(basket, gran):
            hero = None
            if basket:
                hero = gran.create_hero_tale(GingerBreadMan, 'Kolya', basket)
                print(f'Бабка {gran.name} испекла Колобка')
                return hero
            else:
                print('Невозможно создать героя')
                return hero
        return create_main_hero(basket, gran)

    def scene_meeting_enemy(self, enemy, hero, increase_cunning):
        enemy.speak(f'Привет, Колобок {hero.name}! Я {enemy.name}')  # noqa
        enemy.speak(f'{hero.name}, я тебя съем!!!')
        hero.speak('Не ешь меня. Я тебе песенку спаю:')
        hero.cunning += increase_cunning
        for value_sing in hero.sing(enemy.name):
            print(value_sing)
        live_status = enemy.eat_hero(hero.cunning, hero.alive, enemy.cunning)
        return live_status

    def start(self):
        print('Сказка про Колобка:')
        barn = self.barn('flour', 200)
        grandad = self.grandad('Ivan')
        gran = self.gran('Martha')
        main_hero = self.scene_grandad_home(grandad, gran, barn)
        if main_hero:
            main_hero.speak(f'Привет! Я Колобок {main_hero.name}')
            main_hero.speak('Вот такой я получился:')
            print(main_hero.characteristic)
            main_hero.speak('Как видите красивый и сильный!')
            status_roll = main_hero.roll(True)
            if status_roll:
                main_hero.roll(False)
                rabbit = self.enemy('Rabbit')
                live_hero_status = self.scene_meeting_enemy(rabbit, main_hero, 0) # noqa
                if not live_hero_status:
                    print(f'Колобка съел {rabbit.name}')
                    print('Сказки конец!')
                    sys.exit(0)
                status_roll = main_hero.roll(True)
                if status_roll:
                    main_hero.roll(False)
                    wolf = self.enemy('Wolf', 1)
                    live_hero_status = self.scene_meeting_enemy(wolf, main_hero, 1)  # noqa
                    if not live_hero_status:
                        print(f'Колобка съел {wolf.name}!!!')
                        print('Сказки конец!')
                        sys.exit(0)
                    status_roll = main_hero.roll(True)
                    if status_roll:
                        main_hero.roll(False)
                        fox = self.enemy('Fox', 5)
                        live_hero_status = self.scene_meeting_enemy(fox, main_hero, 2)  # noqa
                        if not live_hero_status:
                            fox.speak(f'Колобок я тебе хитрей вот моя хитрость {fox.cunning}') # noqa
                            fox.speak(f'А твоя хитрость {main_hero.cunning}')  # noqa
                            fox.speak(f'Так что колобок {main_hero.name} тебе конец!') # noqa
                            print(f'Колобка съел {fox.name}!')
                            print('Сказки конец!')
                            sys.exit(0)
        else:
            print('Главного героя нет сказка не может продолжаться!')


my_tail = Tale(Stock, Grandad, Gran, Enemy)
my_tail.start()

