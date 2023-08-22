"""
https://acm.timus.ru/problem.aspx?num=1068

Всё, что от вас требуется — найти сумму всех целых чисел,
лежащих между 1 и N включительно.
"""

input_value = int(input())
range_border = abs(input_value) + 1

result = sum(x for x in range(1, range_border)) if input_value != 0 else 1
if input_value < 0:
    result *= -1
    result += 1

print(result)
