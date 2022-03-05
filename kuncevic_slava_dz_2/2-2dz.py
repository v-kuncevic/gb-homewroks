source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
sorted_list = []
for el in source_list:
    if el.isdigit():
        sorted_list.extend(['"', el.zfill(2), '"'])
    elif el[1:].isdigit():
        sorted_list.extend(['"', el.zfill(3), '"'])
    else:
        sorted_list.append(el)
print(' '.join(sorted_list))
