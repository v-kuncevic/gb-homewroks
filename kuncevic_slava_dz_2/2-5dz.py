# очень некрасивая реализация вывода =(
source_list = [57.8, 46.51, 97, 69.2, 4.3, 31.1, 70.4, 444.4, 10.1, 13.3, 3.14, 0.9, 17, 0.01, 1.1, 99.9, 999]
for i in source_list:
    price = f'{i:.2f}'
    print(int(float(price)), 'руб', price[-2:], 'коп,', end=' ')
print()
source_list.sort()
for i in source_list:
    price = f'{i:.2f}'
    print(int(float(price)), 'руб', price[-2:], 'коп,', end=' ')
print()
sorted_list = sorted(source_list, reverse=True)
expensive_list = sorted(sorted_list[:5])
for i in expensive_list:
    price = f'{i:.2f}'
    print(int(float(price)), 'руб', price[-2:], 'коп,', end=' ')
