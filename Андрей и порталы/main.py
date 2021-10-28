"""
Сдать решение задачи 3-Андрей и порталы
Полный балл:	100
Ограничение времени:	1 с
Ограничение памяти:	512M
Ограничение размера стека:	64M
Задача 3: Андрей и порталы
Андрей вот-вот опоздает на школьный этап ВсОШ. К счастью, недавно в его городе появились порталы.

Город, в котором живет Андрей, можно представить в виде прямой. Всего в городе успели построить N порталов. Портал с номером i расположен в точке с координатой xi. Если в текущий момент времени вы находитесь в одной точке с каким-нибудь порталом, то можете всего за одну секунду телепортироваться в любой другой портал вне зависимости от расстояния между ними. А время, требуемое для преодоления расстояния между точками с координатами p и q без использования порталов равно |p − q| секунд. Андрей является влиятельным гражданином, поэтому он может использовать систему порталов любое количество раз.

Изначально Андрей находится в точке s, а точка проведения олимпиады имеет координату e. Помогите Андрею понять, как быстро он может попасть на олимпиаду, ведь каждая секунда на счету.

Входные данные
В первой строке входных данных записано одно целое число s — начальное положение Андрея.

Во второй строке записано одно целое число e — место проведения олимпиады.

В третьей строке записано количество порталов N (2 ≤ N ≤ 2×105).

В каждой из N следующих строк записано целое число xi — координата портала с номером i.

Все числа s, e, xi по модулю не превосходят 108.

Выходные данные
Выведите одно число — минимальное количество секунд, которое потребуется Андрею для того, чтобы добраться до места проведения олимпиады.

Система оценки
Решения, правильно работающие только для случаев, когда N не превосходит 10, будут оцениваться в 20 баллов.

Решения, правильно работающие только для случаев, когда N не превосходит 1000, будут оцениваться в 60 баллов.
"""

x = int(input())
y = int(input())
n = int(input())
x1=abs(x-y)
x2=abs(x-y)
list1=[]
for q in range(n):
    k=int(input())
    list1.append(k)
    if abs(x-k)<x1:
        x1=abs(x-k)
    if abs(y-k)<x2:
        x2=abs(y-k)
g=x1+x2+1
h=abs(x-y)
if g<h:
    print(g)
else: print(h)