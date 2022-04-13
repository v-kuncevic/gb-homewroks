tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) > len(klasses):
    klasses += [None for i in range(len(tutors) - len(klasses))]

result = ((tutors[i], klasses[i]) for i in range(len(tutors)))
print(next(result))
