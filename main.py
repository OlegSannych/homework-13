'''Домашнее задание.
Реализовать простой консольный калькулятор и сделать к нему документацию с помощью sphinx'''


def calculator():
    '''Функция калькулятор выполняет простые математические операции и
    выводит результат операции'''
    try:
        Namber_1 = float(input("Введите первое число: "))
        try:
            Namber_2 = float(input("Введите второе число: "))
            Operation = input("Введите символ операции: ")
            if Operation == "+":
                Result = Namber_1 + Namber_2
                print("Результат", Result)
            elif Operation == "-":
                Result = Namber_1 - Namber_2
                print("Результат", Result)
            elif Operation == "*":
                Result = Namber_1 * Namber_2
                print("Результат", Result)
            elif Operation == "/":
                if Namber_2 != 0:
                    Result = Namber_1 / Namber_2
                    print("Результат: ", Result)
                else:
                    print("Деление на ноль не возможно")
            else:
                print("Введен не верный символ операции")
        except ValueError:
            print('Второе число введено с ошибкой!')
    except ValueError:
        print('Первое число введено с ошибкой!')



if __name__ == '__main__':
    calculator()
