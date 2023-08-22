"""
https://acm.timus.ru/problem.aspx?num=1209

Представим себе бесконечную последовательность цифр,
составленную из записанных друг за другом возрастающих степеней десятки.
Вот начало этой последовательности: 110100100010000…

Всё, что надо — определить, какая цифра находится в такой последовательности
на определённом месте.

Исходные данные

В первой строке находится целое число N (1 ≤ N ≤ 65535).
В i-й из N последующих строк записано целое число
Ki — номер позиции в последовательности (1 ≤ Ki ≤ 2^31 - 1).

Результат
Выведите через пробел N цифр.
i-я цифра должна равняться цифре, которая находится в
описанной выше последовательности на позиции с номером Ki.
"""

import array


task_count = int(input())
positions = array.array('i',(int(input()) for _ in range(task_count)))

max_position = max(positions)

sequence = array.array('B')
degree = 0

while len(sequence) < max_position:
    sequence.append(1)
    sequence += array.array('B', (0 for _ in range(degree)))
    degree += 1

print(' '.join(str(sequence[position - 1]) for position in positions))
