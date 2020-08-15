# Evgeny Baranov
# Homework 13 (finish todolist)

import json
import time
from datetime import datetime


class Item:
    def __init__(self, status_done, info,
                 custom_td=time.strftime("%Y-%m-%d %H:%M:%S"),
                 deadline='infinitely'):
        self.done = status_done
        self.info = info
        self.last_updated = custom_td
        self.deadline = deadline

    def add_deadline(self):
        while True:
            deadline_format = input('Введите время в формате [Год-Месяц-День Час:Минуты:Секунды ]>') # noqa
            try:
                self.deadline = str(datetime.strptime(deadline_format, "%Y-%m-%d %H:%M:%S")) # noqa
                break
            except ValueError:
                print('Неверный формат даты и время!')
                continue

    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'last_updated': str(self.last_updated),
            'deadline': self.deadline
        }


class TodoList:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.file_name = 'tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item['done'], item['info'], item['last_updated'], item['deadline'])) # noqa
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\t {item.last_updated}\t {item.deadline}' # noqa
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.done:
                tasks += f'\n {item.done}\t {item.info}\t {item.last_updated}\t {item.deadline}' # noqa
        return tasks

    def done_task(self, index):
        self.tasks[index].done = True

    def undone_task(self, index):
        self.tasks[index].done = False

    def add_task(self, task):
        self.tasks.append(task)

    def to_json(self):
        with open(self.file_name, 'w') as file:
            tasks = []
            for task in self.tasks:
                tasks.append(task.as_dict())
            json.dump(tasks, file)


class Notification:

    def info_show(self):
        info_list = ['Добро пожаловать в TODO!', 'В этом листе можно хранить любые запись', # noqa
                'Доступны такие действия:', '-"Создать задачу"', '-"Добавить задачу"', # noqa
                '-"Отметить как выполненное"', '-"Отметить как не выполненное"', # noqa
                '-"Показать список задач"', '-"Показать список не выполненных задач"'] # noqa
        for current_value in info_list:
            print(current_value)


class Menu:
    def __init__(self, add_task, on_task, off_task, show_list, not_ready_list, new_task, app_out): # noqa
        self.add_task = add_task
        self.on_task = on_task
        self.off_task = off_task
        self.show_list = show_list
        self.not_ready_list = not_ready_list
        self.new_task = new_task
        self.app_out = app_out

    def info_show(self):
        info_list = ['Меню:', f'Создать задачу - [{self.new_task}]', f'Добавить задачу - [{self.add_task}]', # noqa
            f'Показать не выполненное - [{self.not_ready_list}]', f'Показать список задач - [{self.show_list}]', # noqa
            f'Отметить как "Не выполнено" - [{self.off_task}]', f'Отметить как "Выполнено" -[{self.on_task}]', # noqa
            f'Выйти - [{self.app_out}]'] # noqa
        for current_value in info_list:
            print(current_value)

    def choice(self, todo_list):
        custom_item = None
        while True:
            answer = input('Что делать >')
            if answer == self.app_out:
                todo_list.to_json()
                print('Работа программы завершена')
                break
            if answer == self.new_task:
                while True:
                    answer = input('Укажите описание задачи >')
                    custom_item = Item(False, answer)
                    if len(answer) > 0:
                        break
                while True:
                    answer = input('Указать крайний срок задачи [y/n]>')
                    if answer == 'y':
                        custom_item.add_deadline()
                        break
                    elif answer == 'n':
                        break
                while True:
                    answer = input('Просмотреть созданную задачу [y/n]>')
                    if answer == 'y':
                        print(custom_item.as_dict())
                        break
                    elif answer == 'n':
                        break
                print('Здание создано и готов к добавлению в TODO лист')
            elif answer == self.add_task:
                if not custom_item:
                    print('Задача не создана')
                    continue
                else:
                    print('Задача добавлена')
                    todo_list.add_task(custom_item)
                    todo_list.to_json()
            elif answer == self.not_ready_list:
                not_ready_tasks = todo_list.not_ready_tasks
                if not not_ready_tasks:
                    print('TODO лист пустой')
                print(not_ready_tasks)
            elif answer == self.show_list:
                tasks_list = todo_list.tasks_list
                if not tasks_list:
                    print('TODO лист пустой')
                print(tasks_list)
            elif answer == self.off_task or answer == self.on_task:
                tasks_list = todo_list.tasks_list
                if tasks_list:
                    while True:
                        try:
                            task_index = abs(int(input('Укажите индекс задачи >'))) # noqa
                            if answer == self.off_task:
                                try:
                                    todo_list.undone_task(task_index)
                                    todo_list.to_json()
                                    print(f'Задача под индексом {task_index} отмечена как "не выполнена"') # noqa
                                except IndexError:
                                    print('Нет задачи под таким индексом!')
                                finally:
                                    break
                            elif answer == self.on_task:
                                try:
                                    todo_list.done_task(task_index)
                                    todo_list.to_json()
                                    print(f'Задача под индексом {task_index} отмечена как "выполнена"')  # noqa
                                except IndexError:
                                    print('Нет задачи под таким индексом!')
                                finally:
                                    break
                        except ValueError:
                            print('Введите целое число!')
                            continue
                else:
                    print('Невозможно выполнить, TODO лист пустой')
            else:
                print('Нет такой команды!')
                continue


def main_loop(todo_list):
    while True:
        answer = input('Вы хотите работать с TODO листом? [y/n]>')
        if answer == 'n':
            break
        elif answer == 'y':
            if todo_list:
                print('TODO Лист готов к работе')
                menu = Menu('add', 'on', 'off', 'show', 'not', 'new', 'out')
                menu.info_show()
                menu.choice(todo_list)
                break


def main():
    notification = Notification()
    notification.info_show()
    todo_list = TodoList('default_list', 'default_user')
    main_loop(todo_list)


if __name__ == '__main__':
    main()
