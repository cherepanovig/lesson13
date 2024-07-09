# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает
# True, если строка находится в этом списке, False - если отсутствует.

#Задаем глобальную переменную
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_str = len(string)
    str_up = string.upper()
    str_down = string.lower()
    my_tuple = (len_str, str_up, str_down)
    return (my_tuple)


#string_info('Casablanca')
#string_info('heineken')

def is_contains(string, list_to_search):
    count_calls()
    str_1 = string.upper()  # Приводим строку к верхнему регистру
    list_1 = [item.upper() for item in list_to_search]  # Приводим элементы списка к верхнему регистру
    for i in list_1:  # Проверяем строку на совпадение с элементами списка
        if str_1 == i:
            find = True
        else:
            find = False
    return find


print(string_info('Casablanca'))
print(string_info('Heineken'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)

# Вариант более оптимизированный
print('Оптимизированный вариант:')
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    my_tuple = (len(string), string.upper(), string.lower())
    return (my_tuple)


def is_contains(string, list_to_search):
    count_calls()
    find = string.upper() in [i.upper() for i in list_to_search]  # Ищем вхождение строки в элементах списка
    return find


print(string_info('Casablanca'))
print(string_info('Heineken'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
