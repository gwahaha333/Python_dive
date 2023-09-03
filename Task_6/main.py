import random
from main2 import ferz


def main():
    positions = list(range(1, 9))  # создаём список с числами от 1 до 8
    for i in range(4):  # 4 успешные расстановки
        random.shuffle(positions)  # перемешиваем список
        while not ferz(positions):  # если расстановка не успешная, перемешиваем ещё раз
            random.shuffle(positions)
        print(positions)  # выводим успешную расстановку


if __name__ == '__main__':
    main()