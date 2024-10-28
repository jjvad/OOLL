"""Создать базовый класс с функцией – сумма прогрессии. Создать производные классы:
арифметическая прогрессия и геометрическая прогрессия. Каждый класс имеет два поля типа double.
Первое – первый член прогрессии, второе – постоянная разность (для арифметической) и
постоянное отношение (для геометрической). Определить функцию вычисления суммы,
где параметром является количество элементов прогрессии."""


class Progression:
    def __init__(self, first_digit: float, change_value: float):
        self.__first_digit = first_digit
        self.__change_value = change_value

    @property
    def first_digit(self) -> float:
        return self.__first_digit

    @first_digit.setter
    def first_digit(self, value: float):
        self.__first_digit = value

    @property
    def change_value(self) -> float:
        return self.__change_value

    @change_value.setter
    def change_value(self, value: float):
        self.__change_value = value

    def sum(self, n: int) -> float:
        pass


class ArithmeticProgression(Progression):
    def sum(self, n: int) -> float:
        return n / 2 * (2 * self.first_digit + (n - 1) * self.change_value)


class GeometricProgression(Progression):
    def sum(self, n: int) -> float:
        if self.change_value == 1:
            return self.first_digit * n
        return self.first_digit * (1 - self.change_value ** n) / (1 - self.change_value)


ap = ArithmeticProgression(2.0, 3.0)
gp = GeometricProgression(2.0, 3.0)

print("Сумма арифметической прогрессии:", ap.sum(2))  # 2+5=7
print("Сумма геометрической прогрессии:", gp.sum(2))  # 2+6=8
