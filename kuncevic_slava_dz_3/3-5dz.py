import random


def get_jokes(n, repeat='stopflag'):
    """
    Returns the requested n jokes formed from three random words taken from three lists
    :param n: the number of jokes to be returned
    :type: int
    :param repeat: a flag allowing or prohibiting repetition of words in jokes
    :type: str

    :rtype: list[str]
    :return: the requested number of jokes, truncated by the number of possible repetitions if required
        """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat == 'stopflag':
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


print(get_jokes(n=3, repeat='!=stopflag'))
print(get_jokes(n=11, repeat='!=stopflag'))
print(get_jokes(n=3, repeat='stopflag'))
print(get_jokes(n=11, repeat='stopflag'))
