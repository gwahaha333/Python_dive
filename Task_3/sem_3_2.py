"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
"""

import re
from collections import Counter


def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)


text = ('Чёрная дыра – область пространства, в которой гравитационное'
        ' притяжение настолько сильно, что ни вещество, ни излучение не могут эту'
        ' область покинуть. Для находящихся там тел вторая космическая скорость'
        ' (скорость убегания) должна была бы превышать скорость света, что'
        ' невозможно, поскольку ни вещество, ни излучение не могут двигаться'
        ' быстрее света. Поэтому из черной дыры ничто не может вылететь. Границу'
        ' области, за которую не выходит свет, называют «горизонтом событий», или'
        ' просто «горизонтом» черной дыры.')
print(top_10_words(text))


