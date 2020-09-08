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
