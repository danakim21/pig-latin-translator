def pig_latin_translator(word):
    """
    Returns pig-latin translated word for the given word

    :type word: str
    :rtype: str
    """
    first_char = word[0]
    if (check_if_vowel(first_char)):
        pig_latin = starts_with_vowel(word)
    else:
        pig_latin = starts_with_consonant(word)
    return pig_latin


def check_if_vowel(char):
    """
    Returns if the given character is a vowel

    :type char: str
    :rtype: bool

    ex) "p" => false, "a" => true
    """
    VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return char in VOWELS


def check_if_vowel_with_y(char):
    """
    Returns if the given character is a vowel

    :type char: str
    :rtype: bool

    ex) "p" => false, "a" => true
    """
    VOWELS = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    return char in VOWELS


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
