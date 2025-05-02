# @classmethod и @staticmethod

classmethod в Python — это метод класса, который привязан к самому классу, а не к его экземплярам. Первым аргументом такого метода всегда является сам класс (обычно обозначается как cls), а не экземпляр класса (self).

@staticmethod — это метод, который не имеет доступа ни к атрибутам класса, ни к атрибутам его экземпляров.  Они ведут себя как обычные функции, за исключением того, что могут быть вызваны на уровне класса.

## Разница между classmethod и staticmethod

classmethod принимает cls в качестве первого параметра, в то время как staticmethod не нуждается в конкретных параметрах.
classmethod может обращаться или изменять состояние класса, в то время как staticmethod не может этого делать.

## пример 1

class MyClass:
    param = 5

    @classmethod
    def print_param(cls):
        print(cls.param)

MyClass.print_param() # Вывод: 5

## пример 2

class MyClass:

    @staticmethod
    def print_hello():
        print("Hello, world!")

MyClass.print_hello() # Вывод: Hello, world!
