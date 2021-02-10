def multiple_letter_count(phrase):
    word = phrase.lower()
    res = {ltr: word.count(ltr) for ltr in word}
    return res
    

    """Return dict of {ltr: frequency} from phrase.
        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}
        >>> multiple_letter_count('Yay')
        {'a': 1, 'y': 2}
    """
    
multiple_letter_count('Yay')
