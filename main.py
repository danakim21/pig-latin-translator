def check_if_vowel(char):
    """
    Returns if the given character is a vowel

    :type char: str
    :rtype: bool

    ex) "p" => false, "a" => true
    """
    VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return char in VOWELS


def starts_with_consonant(word):
    """
    Returns translated pig-latin word for the given word when the word starts with a vowel

    :type word: str
    :rtype: str

    ex) "pig" => "igpay", "smile" => "ilesmay"
    """
    vowel_index = 1
    while not (check_if_vowel(word[vowel_index])):
        vowel_index += 1
    return word[vowel_index:] + word[:vowel_index] + "ay"


def starts_with_vowel(word):
    """
    Returns translated pig-latin word for the given word when the word starts with a vowel

    :type word: str
    :rtype: str

    ex) "eat" => "eatway"
    """
    return word + "way"
