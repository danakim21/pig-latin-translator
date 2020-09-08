from check import *


def starts_with_vowel(word):
    """
    Returns the pig-latin translated word for the given word when the word starts with a vowel

    :type word: str
    :rtype: str

    ex) "eat" => "eatway"
    """
    return word + "way"


def starts_with_consonant(word):
    """
    Returns the pig-latin translated word for the given word when the word starts with a vowel

    :type word: str
    :rtype: str

    ex) "pig" => "igpay", "smile" => "ilesmay"
    """
    vowel_index = 1
    while not (check_if_vowel_with_y(word[vowel_index])):
        vowel_index += 1
    return word[vowel_index:] + word[:vowel_index] + "ay"
