"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


while True:
    user_input = int(input('Введите число от 0 до 100000: '))
    if 1 < user_input < 100000:
        k = 0
        for i in range(2, user_input // 2 + 1):
            if user_input % i == 0:
                k = k + 1
        if k <= 0:
            print('Число простое')
        else:
            print('Число не является простым')
        break
    else:
        print('Введите верное число!')
