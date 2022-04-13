n = int(input("До какого значения выдаём нечётные числа? "))
num = (i for i in range(1, n + 1, 2))
for j in num:
    print(j)
