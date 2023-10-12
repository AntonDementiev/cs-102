def plus(num_1, num_2):
    """Операция сложения"""
    return f"Сумма: {num_1 + num_2}"


def minus(num_1, num_2):
    """Операция вычитания"""
    return f"Разность: {num_1 - num_2}"


def multiply(num_1, num_2):
    """Операция умножения"""
    return f"Произведение: {num_1 * num_2}"


def divide(num_1, num_2):
    """Операция деления"""
    return f"Частное: {num_1 / num_2}"


if __name__ == "__main__":
    while True:
        welcome_message = input("Введите операцию: ")
        if welcome_message == "+":
            try:
                print(plus(num_1=float(input()), num_2=float(input())))
            except:
                print("Не ломайте пожалуйста! p.s калькулятор")
        elif welcome_message == "-":
            try:
                print(minus(num_1=float(input()), num_2=float(input())))
            except:
                print("Не ломайте пожалуйста! p.s калькулятор")
        elif welcome_message == "*":
            try:
                print(multiply(num_1=float(input()), num_2=float(input())))
            except:
                print("Не ломайте пожалуйста! p.s калькулятор")
        elif welcome_message == "/":
            try:
                print(divide(num_1=float(input()), num_2=float(input())))
            except ZeroDivisionError:
                print("На ноль делить нельзя !")
            except:
                print("Не ломайте пожалуйста! p.s калькулятор")
        else:
            print("Ошибка операции, введите правильную (+ - * /): ")

