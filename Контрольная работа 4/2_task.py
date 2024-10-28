"""Создать базовый класс «список» на основе обычного массива с  функциями вставки и удаления элементов.
Реализовать на базе списка производные классы стека и очереди."""


class List:
    def __init__(self):
        self.__data = []

    def insert(self, value):
        self.__data.append(value)

    def delete(self, value):
        if value in self.__data:
            self.__data.remove(value)
        else:
            raise ValueError("Элемент не найден в списке")

    def is_empty(self):
        return len(self.__data) == 0

    def get_data(self):
        return self.__data

    def pop_last(self):
        if self.is_empty():
            raise IndexError("Список пустой")
        return self.__data.pop()

    def pop_first(self):
        if self.is_empty():
            raise IndexError("Список пустой")
        return self.__data.pop(0)


class Stack(List):
    def push(self, value):
        self.insert(value)

    def pop(self):
        return self.pop_last()


class Queue(List):
    def enqueue(self, value):
        self.insert(value)

    def dequeue(self):
        return self.pop_first()


spisok = List()
spisok.insert(1)
spisok.insert(2)
spisok.insert([3, 4, 5])
print(spisok.get_data())
print(spisok.pop_first())
print(spisok.pop_last())
print(spisok.get_data())
print(spisok.is_empty())
spisok.delete(2)
print(spisok.is_empty())
print(spisok.get_data())

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
