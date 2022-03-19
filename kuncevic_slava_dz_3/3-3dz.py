import random


def get_jokes(n, repeat):
    """
    Returns the entered n jokes formed from three random words taken from three lists
    :param n: the number of jokes to be returned
    :type: int
    :param repeat: a flag allowing or prohibiting repetition of words in jokes
    :type: str

    :rtype: list[float]
    :return: the requested number of jokes, truncated by the number of possible repetitions if required
    :rtype: str
    :return: input error message if no allow or deny repetition is defined
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat == "stopflag":
        if n > len(nouns):
            noun = random.sample(nouns, len(nouns))
            adverb = random.sample(adverbs, len(nouns))
            adjective = random.sample(adjectives, len(nouns))
            result = [f"{noun[i]} {adverb[i]} {adjective[i]}" for i in range(len(noun))]
            return result
        else:
            noun = random.sample(nouns, n)
            adverb = random.sample(adverbs, n)
            adjective = random.sample(adjectives, n)
            result = [f"{noun[i]} {adverb[i]} {adjective[i]}" for i in range(len(noun))]
            return result

    else:
        noun = random.choices(nouns, k=n)
        adverb = random.choices(adverbs, k=n)
        adjective = random.choices(adjectives, k=n)
        result = [f"{noun[i]} {adverb[i]} {adjective[i]}" for i in range(len(noun))]
        return result


kidding_me = input('Сколько шуточек вам выдать? ')
n = int(kidding_me)
print('Запретить повторы слов в шутках? Y/N ')
repeat = input()
if repeat == 'Y':
    print(get_jokes(n, repeat='stopflag'))
elif repeat == 'N':
    print(get_jokes(n, repeat != 'stopflag'))  # does not equal just for easy reading
else:
    print('Не смешно!')
