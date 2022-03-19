def num_translate(english):
    figures = {'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return figures.get(english)


print(num_translate('six'))
print(num_translate('one'))
print(num_translate('eleven'))
