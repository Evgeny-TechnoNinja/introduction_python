# Evgeny Baranov
# Homework 14 (Person)

class Person:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise ValueError(f'{name} - Wrong value, string needed')
        elif not isinstance(age, int):
            raise ValueError(f'{age} - Wrong value, number needed')
        else:
            self.name = name
            self.age = age
            self.__friends = []

    def add_friend(self, human):
        self.__friends.append(human)

    def is_familiar(self, human):
        if human in self.__friends:
            return True
        return False


print('*********** Run: Task  ************')
# person Bob
bob = Person('Bob', 22)
print(bob.name)
print(bob.age)
# person Robert
robert = Person('Robert', 21)
print(robert.name)
print(robert.age)
# person Sem
sem = Person('Sem', 50)
print(sem.name)
print(sem.age)
# person Jon
jon = Person('Jon', 18)
print(jon.name)
print(jon.age)
# add friends
bob.add_friend(robert)
robert.add_friend(sem)
robert.add_friend(jon)
# friends status
print(robert.is_familiar(sem))
print(bob.is_familiar(robert))
print(bob.is_familiar(sem))
print(sem.is_familiar(robert))
print('************************************')
