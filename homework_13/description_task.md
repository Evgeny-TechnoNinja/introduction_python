# Todolist

## Task
Написать класс, который позволит сохранить список дел, отмечать сделанное и показывать то, что нужно сделать.
Хранить список дел в json файле
При запуске программы должна появится меню с вариантами действий: добавить в список, вывести весь список, вывести
список не сделанных дел, отметить как сделанное

## Что нужно
Дописать список дел



```python
import json


class Item:
    def __init__(self, done, info, last_updated):
        self.done = done
        self.info = info
        self.last_updated = last_updated

    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'last_updated': str(self.last_updated),
        }


class TodoList:
    def __init__(self, name, owner, dead_line):
        self.name = name
        self.owner = owner
        self.dead_line = dead_line
        self.tasks = self.load_tasks()
        self.file_name = 'tasks.json'

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item['done'], item['info'], item['last_updated']))
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\t {item.last_updated}'
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.done:
                tasks += f'\n {item.done}\t {item.info}\t {item.last_updated}'
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

```








