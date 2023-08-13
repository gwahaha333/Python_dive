"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — хэш значения переданного аргумента, а значение — имя аргумента.
Если ключ не хэшируем, используйте его строковое представление.
"""


def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except Exception as e:
            print(e)
            result[str(value)] = key
    return result


print(kwargs_to_dict(username='John', password='qwerty', email='example@mail.com'))
print(kwargs_to_dict(fruits=['apple', 'banana', 'orange']))
print(kwargs_to_dict(languages={'ru': 'Русский', 'en': 'Английский'}))