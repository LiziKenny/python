#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
b = ['n', 1, 4, 'y', 2, -1, 'd', 10.134, [1,2,5,43,94]]
for a in b:
    print(type(a))
    print(type(b))

#2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().
lst = input('Введите элементы для создания списка: ').split()
print(lst)
for el in range(0, len(lst) - 1, 2):
    lst[el], lst[el + 1] = lst[el + 1], lst[el]
print(lst)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
dist = {'winter': [1 , 2, 12], 'sprinq': [3, 4 , 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
mount = int(input('Введите, пожалуйста, номер месяца: '))
for el in dist:
    if mount in dist[el]:
        print(el)
    else:
        print('Такого месяца не существует')
        break

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
str = input('Введите, пожалуйста, предложение: ').lower().split()
print(str)
for num, word in enumerate(str, 1):
    print(f'{num}. {word[:10]}')

#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [8, 10, 5, 6, 3]
print(f'Текущий рейтинг{my_list}')
us = int(input('Введите число: '))
for el in range(len(my_list)):
    if my_list == us:
        my_list.insert(el + 1, us)
        break
    elif my_list[-1] > us:
        my_list.append(us)
    elif my_list[0] < us:
        my_list.insert(0, us)
    elif my_list[el] > us and my_list[el + 1]:
        my_list.insert(el + 1, us)
    print(f'Новый рейтинг{my_list}')
    us = int(input('введите число'))




