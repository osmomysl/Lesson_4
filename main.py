####### Задание 4.
"""
1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
"""
# Открывем святки за март и берем 20 первых имён
names = ('Даниил, Илья, Макар, Никон, Павел, Порфирий, Юлиан, Мария, Михаил, Николай, Роман, Федор, Феодосий, Анна, Василий, Виктор, Владимир, Кузьма, Лев, Архип')
list_20 = names.split(sep = ', ')
print('Список имён:', list_20)

import random
# без инициирования функции
# b = []   # итоговый список
# for i in range(100):
#     a = random.choice(list_20)
#     b.append(a)
# print(type(b), len(b), b)

list_n = []     # глобальная переменная
def f(n):
    '''
    :param n: Количество случайных имён в итоговом списке
    :return: Итоговый список
    '''
    for i in range(n):
        list_n.append(random.choice(list_20))
    return list_n
help(f)
f(100)
print(len(list_n), 'имён: ', f(100))

"""
2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
"""
from collections import Counter

def most_common_name():
    '''
    :return: Самое частое имя из итогового списка и количество упоминаний
    '''
    return print(Counter(list_n).most_common(1))
help(most_common_name)
most_common_name()

"""
3. Напишите функцию вывода самой редкой буквы, с которой начинаются имена в списке на выходе функции F.
"""
def rarest_letter():
    '''
    :return: Самая редкая буква, с которой начинаются имена в итоговом списке, и количество упоминаний
    '''
    list_letters = list(map(lambda x: x[0], list_n))    # формируем список из букв, с которых начинаются имена в list_n
    return print(Counter(list_letters).most_common()[-1:]) # подсчитываем каждую букву и группируем в новый список с указанием частотности
    # [-1:] определяет первое значение с конца в списке, отсортированном по частоте
help(rarest_letter)
rarest_letter()

print()
"""
4.  В файле с логами найти дату самого позднего лога (по метке времени)
"""
'''
1. импорт файла
2. вычленить дату/время
3. разбить строку по дате
4. отсортировать по дате
5. выбрать последнюю дату
'''
import io   # интерфейс ввода/вывода
with io.open('log') as file:
    log = file.read()
# print(log)

import re   # модуль регулярных выражений
def last_date():
    '''
    :return: Дата и время самого позднего лога
    '''
    date_time = re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log)
    date_time = sorted(date_time)
    return print(date_time[-1:])
help(last_date)
last_date()