# С использованием randint вместо первоначально введённого списка
from random import randint

print(a := [randint(0, 100) for j in range(99)], '\n', [i for i in a if a.count(i) == 1], sep='')
