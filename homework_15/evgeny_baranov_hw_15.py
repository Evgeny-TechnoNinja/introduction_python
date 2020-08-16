# Evgeny Baranov
# Homework 15 (Geometric figures)

class Figure:
    def __init__(self, unit_a=0, unit_b=0, unit_c=0, unit_d=0):
        self.unit_d = unit_d
        self.unit_c = unit_c
        self.unit_b = unit_b
        self.unit_a = unit_a


class Triangle(Figure):
    def __init__(self, name, unit_a, unit_b, unit_c):
        super().__init__(unit_a, unit_b, unit_c)
        self.figure_name = name

    def area_triangle(self):
        sp = (self.unit_a + self.unit_b + self.unit_c) / 2
        return (sp * (sp - self.unit_a)
                * (sp - self.unit_b)
                * (sp - self.unit_c)) ** 0.5

    def perimeter_triangle(self):
        result = self.unit_a + self.unit_b + self.unit_b
        return result


class Square(Figure):
    def __init__(self, name, unit_a, unit_b, unit_c, unit_d):
        super().__init__(unit_a, unit_b, unit_c, unit_d)
        self.figure_name = name

    def area_square(self):
        if self.__check_square():
            return self.unit_a * self.unit_a
        return self.__wrong_data()

    def perimeter_square(self):
        if self.__check_square():
            return self.unit_a * 4
        return self.__wrong_data()

    def __check_square(self):
        if self.unit_a == self.unit_b and \
                self.unit_a == self.unit_c and \
                self.unit_a == self.unit_d:
            return True

    def __wrong_data(self):
        return 'Не является квадратом'


class Rectangle(Figure):
    def __init__(self, name, unit_a, unit_b, unit_c, unit_d):
        super().__init__(unit_a, unit_b, unit_c, unit_d)
        self.figure_name = name

    def area_rectangle(self):
        if self.__check_rectangle():
            return self.unit_a * self.unit_b
        return self.__wrong_data()

    def perimeter_rectangle(self):
        if self.__check_rectangle():
            return (self.unit_a + self.unit_b) * 2
        return self.__wrong_data()

    def __check_rectangle(self):
        if self.unit_a == self.unit_c and\
                self.unit_b == self.unit_d:
            return True

    def __wrong_data(self):
        return 'Не является прямоугольником'


print('*********** Run: Task  ************')
triangle = Triangle('triangle', 15, 16, 12)
print(f'Figure: {triangle.figure_name}') # noqa
print(f'S = {triangle.area_triangle()}')
print(f'P = {triangle.perimeter_triangle()}')
print('\n')
square = Square('square', 6, 6, 6, 6)
print(f'Figure: {square.figure_name}')
print(f'S = {square.area_square()}')
print(f'P = {square.perimeter_square()}')
print('\n')
rectangle = Rectangle('rectangle', 6, 12, 6, 12)
print(f'Figure: {rectangle.figure_name}')
print(f'S = {rectangle.area_rectangle()}')
print(f'P = {rectangle.perimeter_rectangle()}')
print('************************************')
