from pyjobs2 import settings
import random


WORDS_LIST = []
with open(settings.FILE_SAMPLE_WORDS, 'rt') as f:
    WORDS_LIST = list(word.strip() for word in f.readlines())
WORDS_LIST_LENGTH = len(WORDS_LIST)


def random_words(count):
    words = []
    for i in range(count):
        pos = random.randint(0, WORDS_LIST_LENGTH-1)
        words.append(WORDS_LIST[pos])

    return words
# ' '.join
