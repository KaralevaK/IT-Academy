# 1. Дан список вида ['1', '11', '12', '22', '2', '13', '30', '33']. Отсортировать его по возрастанию числовых значений,
#  исключив те, квадраты которых являются чётными числами. Программа должна занимать одну строчку.

print(list(map(str,sorted(filter(lambda x: x%2 != 0, map(int,['1', '11', '12', '22', '2', '13', '30', '33']))))))

