def thesaurus(names):
    name_decoding = {}
    for name in names:
        initial = name[0]
        if name_decoding.get(initial):
            name_decoding[initial].append(name)
        else:
            name_decoding.setdefault(initial, [name])
    return name_decoding


staff_names = ("Иван", "Мария", "Петр", "Илья")
name_list = thesaurus(staff_names)
print(name_list)
