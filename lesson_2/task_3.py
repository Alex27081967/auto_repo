import math


def square():
    side = float(input("Введите сторону квадрата: "))
    area = side * side
    return math.ceil(area)


print("Площадь квадрата:", square())
