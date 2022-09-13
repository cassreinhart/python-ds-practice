def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    new_phrase = ''

    if not isinstance(num, int) or num < 0:
        return None
        
    while num > 0:
        new_phrase = phrase + new_phrase
        num = num -1

    return new_phrase
