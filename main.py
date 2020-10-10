from check import *
from start import *


def to_pig_latin(input):
    """
    Returns pig-latin translated word for the given word

    :type word: str
    :rtype: str
    """
    output = []
    split = input.split(" ")
    for word in split:
        first_char = word[0]
        if (check_if_vowel(first_char)):
            pig_latin = starts_with_vowel(word)
        else:
            pig_latin = starts_with_consonant(word)
        output.append(pig_latin)
    return " ".join(output)


def from_pig_latin(word):
    """
    Returns original word from pig-latin 

    :type word: str
    :rtype: str
    """
    return word[:-2]
