"""
Сдать решение задачи 4-Путешествие по джунглям
Полный балл:	100
Ограничение времени:	1 с
Ограничение памяти:	512M
Ограничение размера стека:	64M
Задача 4: Путешествие по джунглям
Горилла Коко очень любит путешествовать по своим родным джунглям с помощью лиан.

Всего в джунглях есть N лиан, расположенных друг за другом и пронумерованных слева направо целыми числами от 1 до N. Расстояние между соседними лианами составляет D метров. Находясь на i-й лиане, Коко может совершить прыжок с нее не более, чем на ai метров вправо. В процессе прыжка Коко должна зацепиться за какую-то другую лиану, мимо которой будет пролетать.

В данный момент Коко висит на первой лиане и хочет переместиться как можно дальше вправо. Помогите Коко и определите максимальный номер лианы, до которой она сможет добраться.

Входные данные
Первая строка входных данных содержит целое число N (2 ≤ N ≤ 105) — количество лиан.

Во второй строке записано целое число D (1 ≤ D ≤ 109) — расстояние между соседними лианами.

В каждой из следующих N строк записано целое число ai (1 ≤ ai ≤ 109) — на сколько метров вправо может прыгнуть Коко, находясь на i-й лиане.

Выходные данные
Выведите единственное целое число — максимальный номер лианы, до которой сможет добраться Коко.

Система оценки
Решения, работающие при N ≤ 15, будут набирать не менее 16 баллов.

Решения, работаюшие при D = 1, будут набирать не менее 12 баллов.

Решения, работающие при N ≤ 2000, будут набирать не менее 56 баллов.
"""

n = int(input())
d = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
k = a[0] // d + 1
for i in range(1, len(a)):
    if i + 1 <= k:
        t = a[i] // d + i + 1
        if k < t:
            k = t
    else:
        break
if k > len(a):
    k = len(a)
print(k)