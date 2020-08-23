# Evgeny Baranov
# Homework 17 (Group of students)

class Group:
    def __init__(self, name_group, description_group):
        self.name = name_group
        self.description = description_group
        self._students = []

    def add_student(self, student):
        self._students.append(student)
        self._note_student()

    def show_students(self):
        if not self._students:
            print(f'Студентов в группе {self.name} нет')
        else:
            for current_value in self._students: # noqa
                print(f'студент: {current_value}') # noqa

    def show_ratings(self):
        list_ratings = self._progress_students()
        print('Показать оценки:')
        for current_value in list_ratings:
            print(current_value)

    def remove_student(self, name):
        index = self._find_index(name)
        if not index:
            print(f'Нет студента с именем {name}')
        else:
            print(f'Студент {name} покидает группу')
            self._clear_student(name)
            self._students.pop(index)

    def transfer_student(self, name, new_group, name_group):
        index = self._find_index(name)
        if not index:
            print(f'Нет студента с именем {name}')
        else:
            for current_value in self._students:
                if current_value.person['name'] == name:
                    new_group._students.append(current_value)
                    current_value.person['group'] = name_group
                    self._students.pop(index)
                    print(f'CV {current_value}')
            print(f'Студент {name} перешёл в группу {name_group}')

    @property
    def get_amount_students(self):
        return len(self._students)

    def _find_index(self, name):
        for current_value in self._students:
            if current_value.person['name'] == name:
                return self._students.index(current_value)

    def _clear_student(self, name):
        for current_value in self._students:
            if current_value.person['name'] == name:
                current_value.person['group'] = None

    def _note_student(self):
        for current_value in self._students:
            if current_value.person['group'] is None:
                current_value.person['group'] = self.name

    def _progress_students(self):
        list_progress = []
        for current_value in self._students:
            current_student = {
                'name': current_value.person['name'],
                'grades': current_value.person['grades']
            }
            list_progress.append(current_student)
        return list_progress


class Student:
    def __init__(self, name, age):
        self.person = {
            'name': name,
            'age': age,
            'grades': [],
            'group': None
        }

    def __str__(self):
        return f'{self.person}'

    def add_rating(self, number):
        if not isinstance(number, int) or number < 1 or number > 12:
            print('Допустимы только числа')
            print('Числа должны быть от 1 до 12')
        else:
            self.person['grades'].append(number)

    def show_rating(self):
        if len(self.person['grades']) == 0:
            print(f'У студента {self.person["name"]} нет оценок')
        else:
            print(f'У студента {self.person["name"]} оценки: {self.person["grades"]}') # noqa

    def show_group(self):
        if not self.person['group']:
            print(f'{self.person["name"]} пока что не в группе')
        else:
            print(f'{self.person["name"]} в группе: {self.person["group"]}')


print('*********** Run: Task  ************')
# people
robert = Student('Robert', 22)
bob = Student('Bob', 21)
sem = Student('Sem', 20)
dent = [robert, bob, sem]
# group dentists
print('**** group dentists ****')
dentists = Group('dentists', 'dentists group desc')
print(f'Имя группы: {dentists.name}')
print(f'Описание: {dentists.description}')
for student_value in dent:
    dentists.add_student(student_value)
print(f'Количество студентов: {dentists.get_amount_students}')
dentists.show_students()
robert.add_rating(1)
robert.add_rating(12)
robert.add_rating(5)
bob.add_rating(10)
bob.add_rating(7)
bob.add_rating(12)
sem.add_rating(5)
sem.add_rating(5)
sem.add_rating(7)
dentists.show_students()
dentists.show_ratings()
bob.show_group()
den = Student('Den', 23)
den.show_group()
den.show_rating()
bob.show_rating()
robert.show_rating()
sem.show_rating()
dentists.remove_student('Bob')
bob.show_group()
dentists.show_students()
# people
raphael = Student('Raphael', 19)
mark = Student('Mark', 20)
alexander = Student('Alexander', 18)
# group cooks
print('**** group cooks ****')
cooks = Group('cooks', 'cooks group desc')
cooks.show_students()
cook = [raphael, mark, alexander]
for student_value in cook:
    cooks.add_student(student_value)
print(f'Количество студентов: {cooks.get_amount_students}')
mark.add_rating(12)
raphael.add_rating(2)
alexander.add_rating(10)
mark.show_group()
cooks.show_ratings()
cooks.transfer_student('Mark', dentists, 'dentists')
dentists.show_students()
mark.show_group()
cooks.show_students()
print('************************************')
